# 🔒 Security and Supply Chain Policy

Packablock ensures zero-trust supply chain validation by treating package manifests and lockfiles as an immutable ledger.

## 🏗️ Architecture

```
                       ┌──────────────────────────────┐
                       │   Local Developer Machine    │
                       │                              │
                       │     package.json/bun.lock    │
                       └──────────────┬───────────────┘
                                      │
                                      │ (pkablk append)
                                      ▼
                       ┌──────────────────────────────┐
                       │      packablock.yaml         │
                       │ (signed cryptographic chain) │
                       └──────────────┬───────────────┘
                                      │
                                      │ (pkablk push)
                                      ▼
┌───────────────────────────────────────────────────────────────────────────┐
│                        Packablock Policy Registry                         │
│                                                                           │
│   Fastify SQL Server (port 3030) <───> Rails Admin Dashboard (port 4000)  │
└───────────────────────────────────────────────────────────────────────────┘
```

## 🛡️ Verification Policies

1. **Lockfile Integrity**: Any dependency mismatch between the lockfile and the signed `packablock.yaml` block ledger will fail CI.
2. **Registry Anchor Validation**: The local ledger must match the registry server's anchor block to guarantee that the manifest hasn't been tampered with or modified retrospectively.
3. **Key Rollover**: Public signing keys are rotated periodically. The rotation boundary is cryptographically recorded in the log using:
   ```bash
   pkablk rollover packablock.yaml -s http://localhost:3030 -t <token>
   ```
