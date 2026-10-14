# Modos de escaneo

Los nombres quick, standard y deep son perfiles operativos de este skill. No se asume que sean flags nativos de Strix. Comprueba `strix --help` y la documentación de la versión instalada antes de construir un comando. Si la herramienta no ofrece un control equivalente, explica la limitación y no simules que se aplicó.

## Quick

Para una primera comprobación de un objetivo concreto y autorizado. Limita el trabajo a descubrimiento de bajo impacto y comprobaciones acotadas. Acordar objetivo, rutas y exclusiones antes de empezar. No usar para redes amplias, enumeración masiva ni explotación.

## Standard

Para evaluar una aplicación o servicio definido con autorización explícita. Especifica dominios/IP exactos, rutas incluidas, exclusiones, ventana temporal, tasa o concurrencia máxima si el CLI lo permite y contacto de emergencia. Revisa resultados antes de cualquier validación activa. No continúes si el proceso genera impacto no previsto.

## Deep

Para evaluación amplia previamente aprobada por escrito por el propietario. Requiere inventario exacto, ventana coordinada, exclusiones, límites técnicos, responsable disponible para detener la prueba y plan de interrupción. Aumenta cobertura de forma gradual. No incluye DoS, persistencia, acceso a datos reales, exfiltración ni evasión. Si el plan carece de límites verificables, detente.

## Registro y entrega

Registra fecha, versión de CLI, perfil, objetivos confirmados, exclusiones y resultado. Guarda salidas localmente con permisos apropiados, redacta secretos y datos sensibles, y comparte solo con destinatarios autorizados. Separa los hallazgos detectados automáticamente de los verificados manualmente; documenta falsos positivos y cobertura no evaluada.
