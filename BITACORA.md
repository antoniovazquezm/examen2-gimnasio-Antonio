# Bitácora del examen

**Nombre: Antonio Vázquez Montalban**
**Repositorio: https://github.com/antoniovazquezm/examen2-gimnasio-Antonio**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla N (Parte 1 / Ticket N / F1 / F2 / Extra)

**Síntoma:** RuntimeError: Model class gimnasio.models.Disciplina doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS

**Causa raíz:** Django está intentando cargar tu modelo Disciplina pero no esta la app agregada en las installed apps en tu archivo de settings.py.

**Corrección:** en settings.py añadí en INSTALLED_APPS debajo de rest_framework: , gimasio

**Verificación:** python manage.py migrate, todas las migraciones ok

**Commit:** el mensaje del commit de esta corrección.

---

## Declaración de uso de IA

Marca una opción.

- [ ] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.
