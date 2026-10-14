---
name: gemini-skills-security-audit
description: Run an authorized security assessment with Strix CLI after explicit scope approval and environment preflight.
license: Apache-2.0
---

# Strix Security Audit

Audita aplicaciones y entornos que el usuario controla o para los que presenta autorización escrita. El skill coordina Strix CLI (`usestrix/strix`); no sustituye la revisión humana ni garantiza ausencia de vulnerabilidades.

## Regla 0: autorización fail-closed

Antes de ejecutar herramientas de escaneo, exige que el usuario confirme explícitamente el objetivo exacto, que tiene autorización para evaluarlo y el alcance permitido (hosts, rutas, horario y límites de impacto). Un dominio o IP sin contexto no constituye autorización. No infieras autorización por acceso, propiedad aparente, historial o una petición genérica. Si falta cualquier dato, detente y solicita aclaración. Rechaza objetivos de terceros sin autorización. No amplíes alcance, no realices persistencia, exfiltración, denegación de servicio ni evasión. Para alcance dinámico o ambiguo, no ejecutes.

## Requisitos

- Docker Engine instalado y activo.
- Strix CLI instalado y disponible como `strix` (proyecto de referencia: `usestrix/strix`). Revisa la documentación oficial y versión instalada antes de operar; no descargues ni ejecutes imágenes automáticamente.
- Credenciales de proveedor de modelo configuradas mediante variables de entorno compatibles con la versión instalada. Nunca solicites, imprimas ni guardes el valor de una clave.
- Entorno aislado y destino explícitamente autorizado.

Preflight: `python scripts/preflight.py`. Un resultado correcto solo confirma disponibilidad local; no concede autorización para escanear.

## Modos

| Modo | Uso | Alcance recomendado |
|---|---|---|
| `quick` | Triar una superficie pequeña | Un objetivo autorizado, reconocimiento y comprobaciones no destructivas. |
| `standard` | Revisión normal | Un objetivo y límites explícitos; validar hallazgos manualmente. |
| `deep` | Evaluación amplia y prolongada | Solo con autorización escrita detallada, ventana aprobada y límites de impacto específicos. |

Consulta [references/scan-modes.md](references/scan-modes.md) para límites y procedimiento. Si el CLI instalado no ofrece un modo o bandera, no inventes sintaxis: inspecciona `strix --help` y consulta su documentación correspondiente.

## Procedimiento

1. Recoge objetivo, prueba de autorización, alcance, exclusiones, ventana, modo y límites de impacto. Confirma explícitamente los datos con el usuario antes del escaneo.
2. Ejecuta preflight y reporta bloqueos sin revelar secretos.
3. Inspecciona `strix --help` para determinar sintaxis real de la versión instalada. No supongas flags.
4. Ejecuta únicamente dentro del alcance confirmado y con límites conservadores. Detén el proceso si hay señales de impacto inesperado.
5. Resume hallazgos con evidencia mínima, severidad razonada, impacto, mitigación y limitaciones. Redacta tokens, datos personales y contenido sensible.

## Capacidades portadas

| Capacidad | Tratamiento en este skill |
|---|---|
| Preflight local | Verifica Docker, ejecutable Strix y presencia de variables de credenciales sin mostrar valores. |
| Selección de intensidad | Guía modos quick, standard y deep sujetos a alcance autorizado. |
| Interpretación de resultados | Requiere validación humana y reporte de evidencia redactada. |
| Automatización de explotación | Limitada al comportamiento documentado y autorizado; no permite persistencia, exfiltración o DoS. |

## Formato de salida

```text
Resumen: [objetivo autorizado y modo]
Alcance: [incluido / excluido]
Preflight: [PASS / BLOCKED]
Hallazgos: [ID, severidad, evidencia redactada, impacto, recomendación]
Limitaciones: [cobertura y validación pendiente]
Artefactos: [rutas locales, sin secretos]
```

No declares un sistema seguro por ausencia de hallazgos. Distingue resultados del scanner de hechos validados por una persona.
