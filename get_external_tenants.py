import os
import csv
import requests
import msal
from collections import defaultdict

TENANT_ID = os.getenv("TENANT_ID")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

GRAPH_SCOPE = ["https://graph.microsoft.com/.default"]
GRAPH_ENDPOINT = "https://graph.microsoft.com/v1.0"

def get_access_token():
    app = msal.ConfidentialClientApplication(
        CLIENT_ID,
        authority=f"https://login.microsoftonline.com/{TENANT_ID}",
        client_credential=CLIENT_SECRET
    )
    result = app.acquire_token_for_client(scopes=GRAPH_SCOPE)
    if "access_token" not in result:
        raise Exception(f"Could not obtain access token: {result}")
    return result["access_token"]

def graph_get_paged(url, token, params=None):
    items = []
    next_url = f"{GRAPH_ENDPOINT}{url}"
    while next_url:
        resp = requests.get(
            next_url,
            headers={"Authorization": f"Bearer {token}"},
            params=params
        )
        if not resp.ok:
            raise Exception(f"Graph GET {next_url} failed: {resp.status_code} {resp.text}")
        data = resp.json()
        items.extend(data.get("value", []))
        next_url = data.get("@odata.nextLink")
        params = None  # nextLink already includes params
    return items

def extract_domain(user):
    # Prefer 'mail'
    mail = user.get("mail")
    if mail and "@" in mail:
        return mail.split("@")[1].lower()

    upn = user.get("userPrincipalName", "")
    if "#EXT#" in upn:
        # Format: original_domain_com#EXT#@yourtenant.onmicrosoft.com
        prefix = upn.split("#EXT#")[0]
        parts = prefix.split("_")
        if len(parts) > 1:
            return parts[-1].lower()

    return None

def main():
    token = get_access_token()
    print("Retrieving guest users...")
    guests = graph_get_paged("/users", token, params={"$filter": "userType eq 'Guest'"})

    domain_map = defaultdict(list)

    for u in guests:
        domain = extract_domain(u)
        if not domain:
            continue
        domain_map[domain].append(u.get("userPrincipalName"))

    rows = []
    for domain, users in domain_map.items():
        rows.append({
            "ExternalDomain": domain,
            "UserCount": len(users),
            "SampleUsers": "; ".join(users[:3])
        })

    rows.sort(key=lambda r: r["UserCount"], reverse=True)

    output_file = "external_tenants.csv"
    with open(output_file, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["ExternalDomain", "UserCount", "SampleUsers"])
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {len(rows)} external domains to {output_file}")

if __name__ == "__main__":
    main()
