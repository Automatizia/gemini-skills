---
name: gemini-skills-session-memory
description: Gesti?n de memoria persistente entre sesiones de trabajo para agentes Gemini y Antigravity, adaptada del concepto de claude-mem (upstream: thedotmack/claude-mem). Almacena decisiones, reglas de arquitectura y contexto clave en SQLite/Markdown sin reexplicaciones.
license: Apache-2.0
---

# Session Memory

Mant?n un registro peque?o y consultable de decisiones de proyecto entre sesiones. Adaptado conceptualmente de [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem); no implica compatibilidad ni afiliaci?n. El usuario controla qu? se conserva y d?nde.

## Configuraci?n y preflight

Define un directorio persistente expl?cito, por ejemplo `.agent-memory/`, y excl?yelo del control de versiones si contiene contexto privado. Ejecuta `python scripts/preflight.py [directorio]` para verificar SQLite y el destino. No guarda informaci?n autom?ticamente.

Elige SQLite para b?squedas estructuradas y Markdown para registros portables o legibles. Protege archivos con permisos locales adecuados; no registres credenciales, tokens, datos personales innecesarios ni contenido confidencial sin autorizaci?n.

## Lectura al inicio

1. Lee primero el ?ndice o resumen m?s reciente.
2. Busca decisiones, restricciones y tareas abiertas relevantes al proyecto actual.
3. Comprueba vigencia frente al repositorio y fuentes actuales; la memoria es una pista, no una verdad garantizada.
4. Cita brevemente el contexto hist?rico relevante al plan de trabajo.

## Guardado al cierre

1. Conserva solo decisiones estables, preferencias expl?citas, reglas de arquitectura y pendientes accionables.
2. A?ade fecha, proyecto, tema, contenido breve y referencias a evidencia local.
3. Actualiza ?ndice/resumen y evita duplicar entradas; marca reemplazos y decisiones obsoletas.
4. No guardes transcripciones completas, secretos ni inferencias presentadas como hechos.

## Recuperaci?n

Busca primero por proyecto y tema; carga ?nicamente las entradas relacionadas. Ante contradicci?n, prevalecen instrucciones actuales del usuario y evidencia vigente. Consulta [references/memory-schema.md](references/memory-schema.md) para el esquema sugerido.
