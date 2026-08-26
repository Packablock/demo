# 🎨 Packablock Supply Chain Trust Registry: E2E Monorepo Demo

A pristine simulation of a real-world polyglot monorepo showing end-to-end (E2E) integration of the **Packablock Zero-Trust Supply Chain Policy Control**.

This workspace serves as a live, self-documenting demo playground that models the workflow of a modern product development team securing their dependencies using `pkablk`.

---

## 🏗️ Monorepo Architecture

This project is a polyglot monorepo managed by **Bun Workspaces** containing a TypeScript service and a Python data processor:

```text
demo/
├── .github/
│   └── workflows/
│       └── ci.yml               # GitHub Actions workflow running supply chain checks
├── docs/                        # MkDocs site source files
│   ├── index.md                 # Welcome page
│   ├── policy.md                # Security architecture documentation
│   └── setup.md                 # Installation and configuration guide
├── packages/
│   ├── typescript-service/      # Bun + TypeScript application (with lodash and zod)
│   │   ├── src/index.ts
│   │   ├── package.json
│   │   └── tsconfig.json
│   └── python-processor/        # Python data processing script (using pyyaml and requests)
│       ├── main.py
│       └── requirements.txt
├── bun.lock                     # Bun monorepo workspace-wide lockfile
├── mkdocs.yml                   # MkDocs project configuration
├── package.json                 # Monorepo workspaces definition
└── packablock.yaml              # Cryptographically signed ledger chain
```

---

## 🚀 Local Setup & Verification

1. **Install dependencies**:
   ```bash
   bun install
   ```

2. **Run the TypeScript service**:
   ```bash
   bun run dev:typescript
   ```

3. **Run the Python script**:
   ```bash
   bun run run:python
   ```

4. **Verify the chain ledger**:
   Install the `pkablk` CLI globally from our source repository:
   ```bash
   bun install -g Packablock/packablock-client
   ```
   Then verify the chain ledger:
   ```bash
   pkablk check packablock.yaml
   ```

5. **Audit dependency drift**:
   Visualise the dependency tree and any unexpected changes:
   ```bash
   pkablk audit packablock.yaml --visualize
   ```

---

## 🛡️ CI/CD Enforcement Policy

The included GitHub Actions workflow [`.github/workflows/ci.yml`](.github/workflows/ci.yml) automates security checks on every pull request:
1. Installs the project dependency tree using `bun install`.
2. Installs the `pkablk` CLI directly from source.
3. Checks the existing `packablock.yaml` cryptographic hashes for integrity.
4. Runs `pkablk audit` to verify constraints.
5. Computes a diff and runs `pkablk append packablock.yaml -l bun.lock` to log updates. If the developer modified `bun.lock` without updating and committing the corresponding block in `packablock.yaml`, the pipeline fails, prompting the developer to run `pkablk append` and commit the updated ledger.
