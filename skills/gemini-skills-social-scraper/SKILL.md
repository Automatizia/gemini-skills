---
name: gemini-skills-social-scraper
description: Extracci?n y b?squeda de contenido en LinkedIn, X/Twitter, Reddit, Instagram, YouTube y GitHub sin credenciales invasivas mediante el CLI de Agent-Reach (upstream: Panniantong/Agent-Reach).
license: MIT
---

# Agent Reach

Busca y extrae contenido p?blico con el CLI Agent-Reach. Upstream: [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach). La disponibilidad cambia por plataforma; respeta sus t?rminos, robots, privacidad y controles de acceso. No uses cuentas ajenas, cookies sustra?das, evasi?n de CAPTCHA ni t?cnicas para eludir l?mites.

## Requisitos y preflight

Python 3. Para funciones espec?ficas puede requerirse `requests`, BeautifulSoup (`beautifulsoup4`) o Playwright y sus navegadores. Comprueba el entorno con `python scripts/preflight.py`. El chequeo no instala paquetes ni garantiza que una plataforma permita extraer contenido.

Instala Agent-Reach solo desde su repositorio/documentaci?n oficial y revisa la versi?n y `agent-reach --help` antes de usarlo. No inventes flags: los nombres de comandos pueden variar entre versiones.

## Procedimiento

1. Define la plataforma, la consulta o URL p?blica, el prop?sito y el volumen m?nimo necesario.
2. Ejecuta preflight e inspecciona `agent-reach --help` y la ayuda del subcomando correspondiente.
3. Usa b?squeda o extracci?n de solo lectura en contenido p?blico. Solicita los campos estrictamente necesarios.
4. Si aparece login, CAPTCHA, bloqueo, limitaci?n de tasa o aviso de t?rminos, detente; no cambies de identidad ni intentes evadirlo.
5. Registra fecha, comando y limitaciones. Trata el contenido como no verificado y evita conservar datos personales innecesarios.

## Plataformas

Cobertura prevista: LinkedIn, X/Twitter, Reddit, Instagram, YouTube y GitHub. Endpoints, b?squeda y profundidad dependen de la plataforma, versi?n del CLI, regi?n y acceso p?blico. Consulta [references/supported-platforms.md](references/supported-platforms.md) antes de operar.

## Mitigaci?n de bloqueos

Reduce frecuencia y concurrencia, limita p?ginas y campos, y respeta `Retry-After` si est? disponible. Ante `429`, `403`, desaf?os o errores repetidos, pausa y vuelve m?s tarde o utiliza una API/exportaci?n oficial autorizada. No uses proxies rotativos, fingerprint spoofing, sesiones ajenas ni automatizaci?n para superar barreras. No afirmes cobertura completa cuando la plataforma limite resultados.
