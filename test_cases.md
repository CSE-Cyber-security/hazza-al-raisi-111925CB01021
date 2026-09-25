# Test Cases – Cybersecurity Asset Inventory System

| # | Test Case | Steps | Expected Result |
|---|-----------|-------|------------------|
| 1 | Add a single asset | Menu → 1 → enter valid Asset ID, Name, Type (e.g. Workstation), IP, OS, Department, Risk Level (e.g. Medium), Status (e.g. Secure) | Asset saved to `data/assets.json`; confirmation message shown |
| 2 | Add asset with duplicate ID | Menu → 1 → enter an Asset ID that already exists | System rejects the ID and re-prompts until a unique ID is entered |
| 3 | Add asset with empty required field | Menu → 1 → press Enter without typing a value for Asset Name | System shows "cannot be empty" warning and re-prompts |
| 4 | Add asset with invalid Asset Type | Menu → 1 → type "Laptop" for Asset Type | System rejects input and re-prompts with valid options (Workstation/Server/Router/Switch/Application) |
| 5 | Add multiple assets at once | Menu → 2 → enter number of assets (e.g. 3) → fill in each asset's details | All 3 assets are added and saved |
| 6 | Display all assets | Menu → 3 | All stored assets printed in formatted block, followed by summary counts (Total, Critical, High, Vulnerable, etc.) |
| 7 | Display with empty inventory | Delete all assets → Menu → 3 | "No assets found." message shown, summary shows all zeros |
| 8 | Search by Asset ID (match) | Menu → 4 → 1 → enter existing ID (e.g. A101) | Matching asset details displayed |
| 9 | Search by Asset ID (no match) | Menu → 4 → 1 → enter non-existent ID | "No matching assets found." shown |
| 10 | Search by partial Asset Name | Menu → 4 → 2 → enter partial name (e.g. "web") | All assets whose name contains "web" (case-insensitive) are shown |
| 11 | Search by Risk Level | Menu → 4 → 3 → enter "Critical" | All Critical-risk assets displayed |
| 12 | Search by Security Status | Menu → 4 → 4 → enter "Vulnerable" | All Vulnerable assets displayed |
| 13 | Update existing asset (partial fields) | Menu → 5 → enter valid ID → leave some fields blank, change others (e.g. new Risk Level) | Only changed fields updated; blank fields retain previous values |
| 14 | Update non-existent asset | Menu → 5 → enter an ID that doesn't exist | "Asset not found." message shown |
| 15 | Update with invalid enum value | Menu → 5 → enter existing ID → type invalid value for Risk Level (e.g. "Extreme") | Warning shown, previous value retained |
| 16 | Delete existing asset (confirmed) | Menu → 6 → enter valid ID → confirm with "y" | Asset removed from inventory and `assets.json` |
| 17 | Delete existing asset (cancelled) | Menu → 6 → enter valid ID → cancel with "n" | Asset remains unchanged; "Deletion cancelled." shown |
| 18 | Delete non-existent asset | Menu → 6 → enter an ID that doesn't exist | "Asset not found." message shown |
| 19 | Security summary counts | Menu → 7, with sample data (1 Critical, 1 High, 1 Medium, 1 Vulnerable) | Summary matches: Total=3, Critical=1, High=1, Medium=1, Vulnerable=1 |
| 20 | Persistence across runs | Add an asset → exit program → relaunch → Menu → 3 | Previously added asset still present (loaded from `data/assets.json`) |
| 21 | Invalid main menu choice | Enter "9" or "abc" at main menu | "Invalid choice" warning shown, menu re-displayed |
