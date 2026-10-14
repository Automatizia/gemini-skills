# Recommendation rules

The auditor uses explicit, deterministic signals and emits suggestions for human review. Rules apply to root-level `package.json` dependencies and recognized filenames discovered outside excluded directories.

| Evidence | Suggested item | Rationale |
|---|---|---|
| `next` dependency or `next.config.*` | `modern-frontend`, `ui-ux-pro-max` | Frontend implementation and interface review may help. |
| `react`, `vue`, `svelte`, or `angular` dependency | `ui-ux-pro-max` | Component interface and interaction review. |
| `Dockerfile`, `docker-compose.yml`, or `compose.yaml` | `strix-security-audit`; `container-build-review` hook | Review container configuration and build changes. Strix still requires explicit target authorization. |
| `pyproject.toml` or `requirements.txt` | `python-project-review` | Python dependency and project convention review. |
| `package.json` | `lint-and-test-before-commit` hook | Candidate lifecycle check; inspect available scripts first. |
| JavaScript/TypeScript source file | Read-only, project-scoped filesystem MCP | Could support repository navigation; restrict access to the project. |

These names are recommendations, not proof that a matching skill or MCP is installed or compatible. Check the current catalog, publisher, permissions, license, and version before setup. The auditor never installs or activates recommendations.
