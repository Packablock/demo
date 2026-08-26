import os
import yaml
import requests

def main():
    print("🐍 python-processor started...")
    
    # Read workspace root packablock configuration if available
    config_path = "../../packablock.yaml"
    if os.path.exists(config_path):
        with open(config_path, 'r') as f:
            try:
                data = yaml.safe_load(f)
                print("🔒 Loaded Packablock policy metadata successfully.")
                print(f"Log type: {data.get('type', 'N/A')}")
                print(f"Chain length: {len(data.get('blocks', []))} blocks")
            except yaml.YAMLError as exc:
                print(f"Error loading packablock.yaml: {exc}")
    else:
        print("⚠️  No packablock.yaml ledger found in workspace root.")

    # Call external API registry health endpoint to demonstrate network connectivity
    print("Checking policy registry server health...")
    try:
        res = requests.get("http://localhost:3030/api/v1/log/pull", timeout=2)
        if res.status_code == 200:
            print("🟢 Policy registry server is running!")
        else:
            print(f"🔴 Policy registry server returned status {res.status_code}")
    except requests.exceptions.RequestException:
        print("🟡 Policy registry server is offline (local standard fallback active).")

if __name__ == "__main__":
    main()
