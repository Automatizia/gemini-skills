# Plataformas soportadas

La integraci?n exacta depende de la versi?n del CLI y de las restricciones de cada servicio. Confirma la sintaxis vigente con `agent-reach --help` y la ayuda del subcomando; los ejemplos siguientes describen el flujo, no flags garantizados.

| Plataforma | Operaci?n orientativa | L?mites frecuentes |
|---|---|---|
| LinkedIn | Buscar publicaciones o leer una URL p?blica | Login frecuente, visibilidad parcial y restricciones estrictas contra automatizaci?n. Detente ante autenticaci?n o desaf?o. |
| X/Twitter | Buscar publicaciones p?blicas por consulta o abrir URL | L?mites de tasa, contenido no visible y cambios de acceso/API. |
| Reddit | Buscar comunidades/publicaciones y abrir hilos p?blicos | Paginaci?n, l?mites de API y borrado/edici?n de contenido. |
| Instagram | Leer perfiles/publicaciones accesibles p?blicamente | Login, consentimiento y bloqueos frecuentes; no extraer contenido privado. |
| YouTube | Buscar videos y obtener metadatos/transcripci?n disponible | Cuotas, regi?n, transcripci?n desactivada o no disponible. |
| GitHub | Buscar repositorios, issues o c?digo p?blico | L?mites de b?squeda/API y contenido sujeto a licencia. No extraer secretos ni datos privados. |

## Flujo de comandos

1. Ejecuta `agent-reach --help` para confirmar el verbo de b?squeda y extracci?n.
2. Usa la consulta o URL como entrada, seg?n la ayuda de la versi?n instalada.
3. Limita resultados y campos; guarda solo lo necesario y anota errores o truncamiento.

Respeta t?rminos de servicio, privacidad, licencias y l?mites de tasa. No hay garant?a de acceso, cobertura ni actualidad. Si requiere login, CAPTCHA o mecanismo anti-bot, detente y usa una API oficial o exportaci?n autorizada.
