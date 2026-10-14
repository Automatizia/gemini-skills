# Automatizia Gemini Skills Ecosystem

**Skills de grado producción para Gemini CLI y Google Antigravity**, adaptados y revisados bajo la doctrina de calidad Bemynd: Anti-Slop, tipado estricto y sandboxing por defecto.

![CI](https://github.com/Automatizia/gemini-skills/actions/workflows/spec.yml/badge.svg) ![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg) ![SemVer](https://img.shields.io/badge/SemVer-2.0.0-informational.svg) ![Matrix](https://img.shields.io/badge/Compatibility-matrix-4c8bf5.svg)

## Propuesta de valor en 30 segundos

Este catálogo oficial open-source reúne skills prácticas para Gemini y Google Antigravity. Cada skill se documenta, valida y mantiene con foco en comportamiento predecible, permisos explícitos, instrucciones claras y uso seguro. Las etiquetas de compatibilidad describen el formato; la validación y certificación de cada skill se publica aquí conforme se incorpora.

## Quick Start

```bash
git clone https://github.com/Automatizia/gemini-skills.git
mkdir -p ~/.gemini/antigravity/skills/gemini-skills-security-audit
cp -R gemini-skills/skills/gemini-skills-security-audit/. ~/.gemini/antigravity/skills/gemini-skills-security-audit/
```

En Windows PowerShell, el destino equivalente es `$HOME\.gemini\antigravity\skills\gemini-skills-security-audit`.

## Compatibilidad

| Cliente | Estado | Notas |
|---|---|---|
| Gemini CLI | Compatible | Usa instrucciones `SKILL.md`; confirma el mecanismo de carga de tu versión. |
| Google Antigravity 2.0 | Objetivo principal | Instalar bajo `~/.gemini/antigravity/skills/`. |
| Claude Code | Adaptación manual | Revisa frontmatter, herramientas y formato antes de instalar. |
| Codex | Adaptación manual | Las skills requieren adaptar metadatos y convenciones del agente. |

## Skills

> **Convención Estricta de Nomenclatura:** Todos los skills en este ecosistema siguen obligatoriamente el formato `gemini-skills-<objetivo>`, donde el sufijo describe con claridad para qué sirve el skill objetivo.

| Skill | Objetivo Operativo | Upstream | Licencia |
|---|---|---|---|
| [gemini-skills-security-audit](skills/gemini-skills-security-audit/SKILL.md) | Pentest y auditoría de seguridad para apps hechas con IA | [usestrix/strix](https://github.com/usestrix/strix) | Apache-2.0 |
| [gemini-skills-social-scraper](skills/gemini-skills-social-scraper/SKILL.md) | Extracción y búsqueda de contenido en redes (LinkedIn, X, Reddit, IG) | [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | MIT |
| [gemini-skills-freellm-gateway](skills/gemini-skills-freellm-gateway/SKILL.md) | Gateway local con 600+ modelos y 7.4B tokens/mes gratuitos | [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | MIT |
| [gemini-skills-session-memory](skills/gemini-skills-session-memory/SKILL.md) | Memoria persistente y contextual cross-session | [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | Apache-2.0 |
| [gemini-skills-project-auditor](skills/gemini-skills-project-auditor/SKILL.md) | Auditor estático de proyectos y recomendador de tooling | claude-code-setup (Anthropic) | Apache-2.0 |

## Propiedad Intelectual y Enlaces Oficiales

Este ecosistema open-source es mantenido por [Automatizia](https://automatizia.com.mx).

* **Portal Corporativo:** [automatizia.com.mx](https://automatizia.com.mx)
* **Fábrica de Software:** [bemynd.com](https://bemynd.com)

> [!IMPORTANT]
> **Deslinde de Propiedad Intelectual:** La plataforma comercial, el motor y las arquitecturas de la **Fábrica de Software Bemynd** son propiedad intelectual privada exclusiva de **Automatizia**. Este repositorio público aloja exclusivamente especificaciones abiertas, herramientas y adaptadores para la comunidad bajo licencias de código abierto (Apache-2.0 y MIT), sin contener lógica interna, datos ni código privado de Automatizia.

## Contribuir y reportar

- [Contributing](CONTRIBUTING.md)
- [Política de seguridad](SECURITY.md)
- [Licencia](LICENSE)

Compatibilidad, revisión y seguridad son específicas de cada skill. Lee la documentación y verifica sus requisitos antes de ejecutarla.
