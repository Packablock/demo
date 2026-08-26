# 📦 Packablock Supply Chain Demo Monorepo

Welcome to the pristine simulation of a real-world polyglot monorepo integrating **Packablock Zero-Trust Supply Chain Policy Control**.

This demo repository demonstrates how developers can secure their package manifests, cryptographically sign local ledger logs, and verify dependencies at build time via CI/CD.

## 🧭 Repository Map

* **`packages/typescript-service`**: A service built with [Bun](https://bun.sh) and TypeScript which uses `lodash` and `zod`.
* **`packages/python-processor`**: A data processor built with Python which parses local configuration data and queries the registry API.
* **`docs/`**: This documentation site, built and served using [MkDocs Material](https://squidfunk.github.io/mkdocs-material/).
* **`packablock.yaml`**: The local cryptographic ledger holding verified package attestation blocks.

## 🚀 Key Integration Features

1. **Local Integrity Chains**: Each package lockfile updates is tracked as a signed, cryptographic block inside `packablock.yaml`.
2. **Offline Standalone Auditing**: Run `pkablk audit packablock.yaml --visualize` to see dependency drift instantly.
3. **GitHub Actions E2E Enforcement**: Every pull request installs, appends, checks, and validates the dependency tree.
