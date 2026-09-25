"""
Cybersecurity Asset Inventory System
-------------------------------------
Add, search, update, delete, and display an organization's IT assets,
classified by asset type, risk level, and security status.

Run:
    python asset_inventory.py
"""

import json
import os

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "assets.json")

ASSET_TYPES = ["Workstation", "Server", "Router", "Switch", "Application"]
RISK_LEVELS = ["Low", "Medium", "High", "Critical"]
SECURITY_STATUSES = ["Secure", "Warning", "Vulnerable"]


# --------------------------------------------------------------------------
# Persistence
# --------------------------------------------------------------------------
def load_assets():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []


def save_assets(assets):
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(assets, f, indent=2)


# --------------------------------------------------------------------------
# Input validation helpers
# --------------------------------------------------------------------------
def get_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("  ⚠ This field cannot be empty. Please try again.")


def get_choice(prompt, choices):
    choice_str = "/".join(choices)
    while True:
        value = input(f"{prompt} ({choice_str}): ").strip().title()
        if value in choices:
            return value
        print(f"  ⚠ Invalid choice. Must be one of: {choice_str}")


def get_unique_asset_id(assets, prompt="Asset ID: "):
    existing_ids = {a["asset_id"].upper() for a in assets}
    while True:
        asset_id = get_non_empty(prompt)
        if asset_id.upper() in existing_ids:
            print("  ⚠ Asset ID already exists. Please enter a unique ID.")
        else:
            return asset_id


def find_asset(assets, asset_id):
    for asset in assets:
        if asset["asset_id"].upper() == asset_id.upper():
            return asset
    return None


# --------------------------------------------------------------------------
# Core operations
# --------------------------------------------------------------------------
def add_asset(assets):
    print("\n--- Add New Asset ---")
    asset_id = get_unique_asset_id(assets)
    asset = {
        "asset_id": asset_id,
        "asset_name": get_non_empty("Asset Name: "),
        "asset_type": get_choice("Asset Type", ASSET_TYPES),
        "ip_address": get_non_empty("IP Address: "),
        "os": get_non_empty("Operating System: "),
        "department": get_non_empty("Owner/Department: "),
        "risk_level": get_choice("Risk Level", RISK_LEVELS),
        "security_status": get_choice("Security Status", SECURITY_STATUSES),
    }
    assets.append(asset)
    save_assets(assets)
    print(f"  ✔ Asset '{asset_id}' added successfully.")


def add_multiple_assets(assets):
    try:
        count = int(input("\nEnter number of assets: ").strip())
    except ValueError:
        print("  ⚠ Please enter a valid number.")
        return
    for i in range(1, count + 1):
        print(f"\nAsset {i}")
        add_asset(assets)


def display_asset(asset):
    print("-----------------------------------------")
    print(f"Asset ID    : {asset['asset_id']}")
    print(f"Asset Name  : {asset['asset_name']}")
    print(f"Asset Type  : {asset['asset_type']}")
    print(f"IP Address  : {asset['ip_address']}")
    print(f"OS          : {asset['os']}")
    print(f"Department  : {asset['department']}")
    print(f"Risk Level  : {asset['risk_level']}")
    print(f"Status      : {asset['security_status']}")


def display_all_assets(assets):
    print("\n=========================================")
    print(" CYBERSECURITY ASSET INVENTORY")
    print("=========================================")
    if not assets:
        print("No assets found.")
    else:
        for asset in assets:
            display_asset(asset)
    print("-----------------------------------------")
    print_summary(assets)


def search_asset(assets):
    print("\n--- Search Asset ---")
    print("1. Search by Asset ID")
    print("2. Search by Asset Name")
    print("3. Search by Risk Level")
    print("4. Search by Security Status")
    sub_choice = input("Choose search type: ").strip()

    results = []
    if sub_choice == "1":
        asset_id = get_non_empty("Enter Asset ID: ")
        asset = find_asset(assets, asset_id)
        results = [asset] if asset else []
    elif sub_choice == "2":
        name = get_non_empty("Enter Asset Name (partial ok): ").lower()
        results = [a for a in assets if name in a["asset_name"].lower()]
    elif sub_choice == "3":
        level = get_choice("Enter Risk Level", RISK_LEVELS)
        results = [a for a in assets if a["risk_level"] == level]
    elif sub_choice == "4":
        status = get_choice("Enter Security Status", SECURITY_STATUSES)
        results = [a for a in assets if a["security_status"] == status]
    else:
        print("  ⚠ Invalid option.")
        return

    if results:
        print(f"\nFound {len(results)} matching asset(s):")
        for asset in results:
            display_asset(asset)
    else:
        print("  No matching assets found.")


def update_asset(assets):
    print("\n--- Update Asset ---")
    asset_id = get_non_empty("Enter Asset ID to update: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print("  ⚠ Asset not found.")
        return

    print("Leave field blank to keep current value.")
    display_asset(asset)

    name = input(f"Asset Name [{asset['asset_name']}]: ").strip()
    if name:
        asset["asset_name"] = name

    asset_type = input(f"Asset Type [{asset['asset_type']}] ({'/'.join(ASSET_TYPES)}): ").strip().title()
    if asset_type:
        if asset_type in ASSET_TYPES:
            asset["asset_type"] = asset_type
        else:
            print("  ⚠ Invalid asset type, keeping previous value.")

    ip = input(f"IP Address [{asset['ip_address']}]: ").strip()
    if ip:
        asset["ip_address"] = ip

    os_name = input(f"Operating System [{asset['os']}]: ").strip()
    if os_name:
        asset["os"] = os_name

    dept = input(f"Department [{asset['department']}]: ").strip()
    if dept:
        asset["department"] = dept

    risk = input(f"Risk Level [{asset['risk_level']}] ({'/'.join(RISK_LEVELS)}): ").strip().title()
    if risk:
        if risk in RISK_LEVELS:
            asset["risk_level"] = risk
        else:
            print("  ⚠ Invalid risk level, keeping previous value.")

    status = input(f"Security Status [{asset['security_status']}] ({'/'.join(SECURITY_STATUSES)}): ").strip().title()
    if status:
        if status in SECURITY_STATUSES:
            asset["security_status"] = status
        else:
            print("  ⚠ Invalid security status, keeping previous value.")

    save_assets(assets)
    print(f"  ✔ Asset '{asset_id}' updated successfully.")


def delete_asset(assets):
    print("\n--- Delete Asset ---")
    asset_id = get_non_empty("Enter Asset ID to delete: ")
    asset = find_asset(assets, asset_id)
    if not asset:
        print("  ⚠ Asset not found.")
        return
    display_asset(asset)
    confirm = input("Are you sure you want to delete this asset? (y/n): ").strip().lower()
    if confirm == "y":
        assets.remove(asset)
        save_assets(assets)
        print(f"  ✔ Asset '{asset_id}' deleted successfully.")
    else:
        print("  Deletion cancelled.")


def print_summary(assets):
    total = len(assets)
    critical = sum(1 for a in assets if a["risk_level"] == "Critical")
    high = sum(1 for a in assets if a["risk_level"] == "High")
    medium = sum(1 for a in assets if a["risk_level"] == "Medium")
    low = sum(1 for a in assets if a["risk_level"] == "Low")
    vulnerable = sum(1 for a in assets if a["security_status"] == "Vulnerable")
    warning = sum(1 for a in assets if a["security_status"] == "Warning")
    secure = sum(1 for a in assets if a["security_status"] == "Secure")

    print("=========================================")
    print(f"Total Assets      : {total}")
    print(f"Critical Assets   : {critical}")
    print(f"High Risk Assets  : {high}")
    print(f"Medium Risk Assets: {medium}")
    print(f"Low Risk Assets   : {low}")
    print(f"Vulnerable Assets : {vulnerable}")
    print(f"Warning Assets    : {warning}")
    print(f"Secure Assets     : {secure}")
    print("=========================================")


# --------------------------------------------------------------------------
# Menu / main loop
# --------------------------------------------------------------------------
def print_menu():
    print("\n========== CYBERSECURITY ASSET INVENTORY SYSTEM ==========")
    print("1. Add Asset")
    print("2. Add Multiple Assets")
    print("3. Display All Assets")
    print("4. Search Asset")
    print("5. Update Asset")
    print("6. Delete Asset")
    print("7. Security Summary")
    print("8. Exit")
    print("============================================================")


def main():
    assets = load_assets()
    while True:
        print_menu()
        choice = input("Enter your choice (1-8): ").strip()

        if choice == "1":
            add_asset(assets)
        elif choice == "2":
            add_multiple_assets(assets)
        elif choice == "3":
            display_all_assets(assets)
        elif choice == "4":
            search_asset(assets)
        elif choice == "5":
            update_asset(assets)
        elif choice == "6":
            delete_asset(assets)
        elif choice == "7":
            print_summary(assets)
        elif choice == "8":
            print("Exiting Cybersecurity Asset Inventory System. Goodbye!")
            break
        else:
            print("  ⚠ Invalid choice. Please enter a number between 1 and 8.")


if __name__ == "__main__":
    main()
