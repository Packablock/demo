# 🛠️ Setup and Installation Guide

Follow these steps to initialize and run the Packablock demo monorepo locally.

## 📋 Prerequisites

Ensure you have the following system utilities installed:
* [Bun](https://bun.sh) (v1.0 or later)
* Python (v3.9 or later)

Our client CLI tool `pkablk` will be installed globally automatically via the project initialization or GitHub actions.

## 🚀 Running the Local Project

### 1. Install Workspace Dependencies
Install node dependencies using Bun in the monorepo root:
```bash
bun install
```

### 2. Install Python Dependencies
Create a virtual environment and install the required modules:
```bash
cd packages/python-processor
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd ../..
```

### 3. Initialize the Packablock Ledger
If you are initializing a new project ledger:
```bash
bun install -g Packablock/packablock-client
pkablk init packablock.yaml -d "Initial monorepo supply chain genesis block"
```

### 4. Append Changes to the Manifest
Whenever dependencies in `bun.lock` (or other lockfiles) are modified, append them to the ledger:
```bash
pkablk append packablock.yaml -l bun.lock
```
