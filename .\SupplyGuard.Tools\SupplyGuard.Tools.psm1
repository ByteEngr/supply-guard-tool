New-SupplyGuardSupplier `
    -SupplierName "Contoso Logistics" `
    -SupplierDomain "contoso-logistics.com" `
    -SupplierUsers "alice@contoso-logistics.com","bob@contoso-logistics.com" `
    -ExpiryDays 90 `
    -SharePointAdminUrl "https://yourtenant-admin.sharepoint.com" `
    -SensitivityLabelId "00000000-0000-0000-0000-000000000000" `
    -DlpPolicyName "Supply Chain – External Collaboration"
Get-SupplyGuardExternalTenantSummary -OutputPath .\ExternalTenants.csv
