# Automatizia Gemini Skills Ecosystem

**Skills de grado producción para Gemini CLI y Google Antigravity**, adaptados y revisados bajo la doctrina de calidad Bemynd: Anti-Slop, tipado estricto y sandboxing por defecto.

![CI](https://github.com/Automatizia/gemini-skills/actions/workflows/spec.yml/badge.svg) ![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg) ![SemVer](https://img.shields.io/badge/SemVer-2.0.0-informational.svg) ![Matrix](https://img.shields.io/badge/Compatibility-matrix-4c8bf5.svg)

## Propuesta de valor en 30 segundos

Este catálogo oficial open-source reúne skills prácticas para Gemini y Google Antigravity. Cada skill se documenta, valida y mantiene con foco en comportamiento predecible, permisos explícitos, instrucciones claras y uso seguro. Las etiquetas de compatibilidad describen el formato; la validación y certificación de cada skill se publica aquí conforme se incorpora.

## Quick Start

```bash
git clone https://github.com/Automatizia/gemini-skills.git
mkdir -p ~/.gemini/antigravity/skills/strix-security-audit
cp -R gemini-skills/skills/strix-security-audit/. ~/.gemini/antigravity/skills/strix-security-audit/
```

En Windows PowerShell, el destino equivalente es `$HOME\.gemini\antigravity\skills\strix-security-audit`.

## Compatibilidad

| Cliente | Estado | Notas |
|---|---|---|
| Gemini CLI | Compatible | Usa instrucciones `SKILL.md`; confirma el mecanismo de carga de tu versión. |
| Google Antigravity 2.0 | Objetivo principal | Instalar bajo `~/.gemini/antigravity/skills/`. |
| Claude Code | Adaptación manual | Revisa frontmatter, herramientas y formato antes de instalar. |
| Codex | Adaptación manual | Las skills requieren adaptar metadatos y convenciones del agente. |

## Skills

| Skill | Estado | Descripción |
|---|---|---|
| [strix-security-audit](skills/strix-security-audit/SKILL.md) | Disponible | Orquesta auditorías autorizadas con Strix CLI y controles fail-closed. |

## Contribuir y reportar

- [Contributing](CONTRIBUTING.md)
- [Política de seguridad](SECURITY.md)
- [Licencia](LICENSE)

Compatibilidad, revisión y seguridad son específicas de cada skill. Lee la documentación y verifica sus requisitos antes de ejecutarla.
