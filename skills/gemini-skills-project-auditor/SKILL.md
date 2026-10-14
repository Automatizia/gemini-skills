---
name: gemini-skills-project-auditor
description: Auditor est?tico de repositorios que inspecciona la estructura de c?digo, dependencias y configuraci?n para recomendar autom?ticamente skills, hooks de ciclo de vida y servidores MCP ?ptimos para Gemini y Antigravity (adaptado de claude-code-setup de Anthropic).
license: Apache-2.0
---

# Project Setup Auditor

Audita est?ticamente un repositorio local y sugiere herramientas seg?n archivos y dependencias observables. Adaptado del enfoque de claude-code-setup de Anthropic; no es una herramienta oficial de Anthropic. No instala skills, hooks ni MCPs, ni ejecuta c?digo del proyecto.

## Ejecuci?n

Ejecuta `python scripts/audit_project.py <directorio> [--format json|markdown]`. El valor predeterminado es el directorio actual y el formato JSON. El resultado incluye evidencias detectadas, skills, hooks y MCPs sugeridos, adem?s de limitaciones. Revisa [references/recommendation-rules.md](references/recommendation-rules.md) para las heur?sticas.

## Procedimiento

1. Confirma la ra?z del proyecto y excluye directorios con datos sensibles o volumen innecesario.
2. Ejecuta el auditor en modo de solo lectura. Analiza nombres de archivos y manifiestos comunes: `package.json`, `requirements.txt`, `pyproject.toml`, `Dockerfile` y configuraci?n relacionada.
3. Revisa evidencias, advertencias y recomendaciones; una dependencia declarada no demuestra uso activo ni necesidad.
4. Presenta sugerencias como opciones para revisi?n humana. Confirma compatibilidad y origen antes de instalar o configurar cualquier herramienta.
5. No inspecciones `.env`, llaves, credenciales, archivos de usuario, dependencias vendorizadas ni contenido de `node_modules`, `.git` o entornos virtuales.

Los hooks y MCP sugeridos son ideas de configuraci?n; este script no modifica el proyecto. La heur?stica puede producir falsos positivos y no sustituye una revisi?n de arquitectura, seguridad o requisitos del equipo.
