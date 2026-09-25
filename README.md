# Week 01 – Cybersecurity Asset Inventory System

A command-line tool for managing an organization's IT assets: adding, searching,
updating, deleting, and displaying computers, servers, routers, switches, and
applications, each classified by **Asset Type**, **Risk Level**, and **Security Status**.

## Repository Structure

```
Week-01-Cybersecurity-Asset-Inventory/
├── src/
│   └── asset_inventory.py
├── data/
│   └── assets.json
├── tests/
│   └── test_cases.md
├── screenshots/
│   ├── 01-add-asset.png
│   ├── 02-display-assets.png
│   ├── 03-search-asset.png
│   ├── 04-update-asset.png
│   ├── 05-delete-asset.png
│   ├── 06-security-summary.png
│   └── 07-input-validation.png
└── README.md
```

## Features

- **Add Asset** – add one asset, with input validation and duplicate-ID checking
- **Add Multiple Assets** – bulk entry, prompts for a count then loops
- **Display All Assets** – formatted listing plus a security summary
- **Search Asset** – by Asset ID, Asset Name (partial match), Risk Level, or Security Status
- **Update Asset** – edit any field, blank input keeps the current value
- **Delete Asset** – with confirmation prompt
- **Security Summary** – total assets, counts by risk level, counts by security status
- **Persistence** – all data is saved to `data/assets.json` after every change, and reloaded on startup

## Data Fields

| Field | Notes |
|---|---|
| Asset ID | Must be unique |
| Asset Name | Free text |
| Asset Type | Workstation / Server / Router / Switch / Application |
| IP Address | Free text |
| Operating System | Free text |
| Owner/Department | Free text |
| Risk Level | Low / Medium / High / Critical |
| Security Status | Secure / Warning / Vulnerable |

## How to Run

```bash
cd src
python asset_inventory.py
```

You'll see a menu:

```
========== CYBERSECURITY ASSET INVENTORY SYSTEM ==========
1. Add Asset
2. Add Multiple Assets
3. Display All Assets
4. Search Asset
5. Update Asset
6. Delete Asset
7. Security Summary
8. Exit
============================================================
```

## Sample Output

```
=========================================
 CYBERSECURITY ASSET INVENTORY
=========================================
-----------------------------------------
Asset ID    : A101
Asset Name  : HR-PC-01
Asset Type  : Workstation
IP Address  : 192.168.1.10
OS          : Windows 11
Department  : HR
Risk Level  : Medium
Status      : Secure
-----------------------------------------
Asset ID    : A102
Asset Name  : Web-Server
Asset Type  : Server
IP Address  : 192.168.1.20
OS          : Ubuntu
Department  : IT
Risk Level  : Critical
Status      : Vulnerable
-----------------------------------------
Asset ID    : A103
Asset Name  : Core-Router
Asset Type  : Router
IP Address  : 192.168.1.1
OS          : Cisco IOS
Department  : Network
Risk Level  : High
Status      : Warning
-----------------------------------------
=========================================
Total Assets      : 3
Critical Assets   : 1
High Risk Assets  : 1
Medium Risk Assets: 1
Low Risk Assets   : 0
Vulnerable Assets : 1
Warning Assets    : 1
Secure Assets     : 1
=========================================
```

## Testing

See [`tests/test_cases.md`](tests/test_cases.md) for the full manual test matrix
(21 cases covering add, search, update, delete, validation, and persistence).

## Screenshots

Place terminal screenshots of each feature in `screenshots/`, named to match
the required structure (`01-add-asset.png` through `07-input-validation.png`).
