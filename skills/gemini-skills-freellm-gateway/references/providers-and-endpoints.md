# Proveedores y endpoints

FreeLLM upstream describe un cat?logo amplio (m?s de 600 modelos y 34 proveedores seg?n su presentaci?n). La lista y las cuotas var?an; obt?n los valores actuales de la documentaci?n o del endpoint de modelos de la instancia. No se fija aqu? una lista est?tica que pueda quedar obsoleta.

## Compatibilidad de rutas

| Familia | Uso com?n | Confirmaci?n necesaria |
|---|---|---|
| OpenAI-compatible | Chat completions y cat?logo de modelos | Confirma base URL y rutas exactas con la versi?n local; un patr?n habitual es `/v1/chat/completions`. |
| Anthropic-compatible | Messages API | Confirma soporte y ruta exacta; un patr?n habitual es `/v1/messages`. |

Algunos gateways traducen esquemas; compatibilidad de endpoint no garantiza igualdad de par?metros, herramientas, streaming o formatos de respuesta. Usa modelos anunciados por la instancia y revisa la documentaci?n para autenticaci?n y l?mites.

## Proveedores

El cat?logo puede incluir proveedores con planes gratuitos, comunitarios o cuotas promocionales. Consulta la instancia/documentaci?n para nombres y disponibilidad vigentes. Verifica ubicaci?n de procesamiento, retenci?n, l?mites y condiciones de cada proveedor antes de enviar datos. Si un modelo falla o agota cuota, selecciona otro modelo compatible presente en el cat?logo, reduce tokens y limita reintentos.
