---
name: gemini-skills-freellm-gateway
description: Gateway local compatible con APIs de LLM que enruta consultas hacia m?s de 600 modelos y 34 proveedores con cuota gratuita mensual de tokens (upstream: tashfeenahmed/freellmapi). ?sala para tareas batch o desarrollo sin agotar cuotas premium.
license: MIT
---

# FreeLLM Gateway

FreeLLM API ofrece un gateway local para desarrollo y tareas batch. Upstream: [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi). La cantidad de modelos, proveedores, disponibilidad y cuota gratuita puede cambiar; verifica la informaci?n del proyecto y los t?rminos vigentes. No env?es datos sensibles a proveedores externos sin autorizaci?n.

## Inicio local

Requisitos: Node.js y `npx`. Revisa el paquete y su versi?n antes de ejecutarlo. Para iniciar, usa el comando documentado por upstream, por ejemplo `npx freellmapi`; no aceptes prompts de instalaci?n inesperados sin revisar el paquete. Mant?n el servidor ligado a localhost y confirma el puerto mostrado por el proceso (normalmente 8000 o 3000). No lo expongas a la red.

Ejecuta `python scripts/preflight.py` para revisar Node, npx y disponibilidad de puertos candidatos. No inicia el gateway ni instala dependencias.

## Endpoints y uso

Consulta [references/providers-and-endpoints.md](references/providers-and-endpoints.md) y la documentaci?n del paquete instalado para conocer rutas exactas. En general, el gateway expone una API local compatible con OpenAI y puede ofrecer una ruta Anthropic compatible. Usa el endpoint y formato que anuncie la versi?n local; no supongas que una ruta existe.

Configura el SDK cliente con base URL local y la clave de desarrollo requerida por el gateway. No registres claves ni cuerpos sensibles en logs. Una API local no implica que las solicitudes se procesen localmente: el gateway puede reenviarlas a proveedores externos.

## Procedimiento

1. Inspecciona versi?n, licencia, documentaci?n y `--help` del paquete.
2. Ejecuta preflight y arranca el comando upstream en una terminal local.
3. Consulta el endpoint de modelos documentado o la lista publicada por la instancia.
4. Elige un modelo compatible y de baja sensibilidad; env?a una solicitud m?nima.
5. Ante cuota agotada, error de proveedor o modelo indisponible, selecciona otro proveedor/modelo anunciado y compatible. No reintentes indefinidamente.
6. Det?n el proceso al terminar y evita publicar el puerto.

Free tier y disponibilidad est?n sujetos a cambios. Para producci?n, privacidad, fiabilidad o trabajos cr?ticos, eval?a directamente el proveedor y sus condiciones.
