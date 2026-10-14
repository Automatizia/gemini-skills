# Contribuir

Gracias por proponer una mejora. Mantén cada cambio enfocado, revisable y seguro.

## Añadir o cambiar un skill

1. Abre un issue para describir el caso de uso, cliente objetivo y límites de seguridad; para cambios pequeños, puedes abrir directamente un PR.
2. Crea `skills/<nombre-kebab-case>/SKILL.md`. El nombre de carpeta debe coincidir exactamente con el campo `name` del frontmatter.
3. Añade solo los recursos necesarios, por ejemplo `scripts/` y `references/`. Documenta requisitos, permisos, entradas, salidas, fallos y ejemplos seguros.
4. Declara herramientas y dependencias, fija versiones cuando sea posible y no incluyas secretos, datos reales ni instrucciones de acceso no autorizado.
5. Ejecuta localmente `python scripts/validate_skills.py` y `python -m py_compile skills/<nombre>/scripts/*.py` cuando existan scripts Python. Revisa el YAML y Markdown con los linters del workflow.
6. Abre un pull request con propósito, impacto, validación realizada y cualquier limitación de compatibilidad.

## Estructura sugerida

```text
skills/<nombre>/
├── SKILL.md
├── scripts/       # herramientas pequeñas y deterministas, si aplican
└── references/    # guías técnicas de apoyo, si aplican
```

## Checklist de calidad

- [ ] El frontmatter YAML contiene `name`, `description` y `license` válidos.
- [ ] El nombre de `name` coincide con la carpeta y usa kebab-case.
- [ ] Las instrucciones son concretas, reproducibles y delimitan entradas y permisos.
- [ ] El comportamiento falla de forma segura ante ambigüedad, falta de autorización o dependencia ausente.
- [ ] Se ejecutó `python scripts/validate_skills.py`; las pruebas pertinentes están descritas.
- [ ] Ningún archivo supera 1,000 líneas; no hay secretos, datos privados ni contenido generado innecesario.
- [ ] Se revisaron licencia, atribución y compatibilidad declarada.

Al enviar una contribución, aceptas que se distribuya bajo Apache-2.0, sujeto a los términos de dicha licencia.
