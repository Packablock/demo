import os
import yaml
import requests

def main():
    print("🐍 python-processor started...")
    
    # Read workspace root packablock configuration if available
    script_dir = os.path.dirname(os.path.abspath(__file__))
    candidates = [
        os.path.join(script_dir, "../../packablock.yaml"),
        os.path.join(os.getcwd(), "packablock.yaml"),
        "packablock.yaml",
    ]
    config_path = next((p for p in candidates if os.path.exists(p)), None)
    if config_path:
        with open(config_path, 'r') as f:
            try:
                docs = list(yaml.safe_load_all(f))
                meta_blocks = [d for d in docs if isinstance(d, dict) and "$yaml-chain-meta" in d]
                print("🔒 Loaded Packablock policy metadata successfully.")
                print(f"Total YAML documents: {len(docs)}")
                print(f"Chain length: {len(meta_blocks)} blocks")
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
