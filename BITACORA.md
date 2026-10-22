# Bitácora del examen

**Nombre: Antonio Vázquez Montalban**
**Repositorio: https://github.com/antoniovazquezm/examen2-gimnasio-Antonio**

Copia el bloque de abajo una vez por cada falla que encuentres. Llénalo en el momento, no al final.

---

## Falla 2 (Parte 1 / Ticket N / F1 / F2 / Extra)

**Síntoma:** IntegrityError: UNIQUE constraint failed: gimnasio_disciplina.nombre

**Causa raíz:** cada vez que se leía una clase, se intentaba crear una nueva disciplina

**Corrección:** ingresar al archivo de carga de datos y cambiar la linea de disciplina por: disciplina, _ = Disciplina.objects.get_or_create(nombre=fila["disciplina"])

Pegué el error en google y gemini corrigió la línea, pero antes me dio el link a la documentación de Django: Si la disciplina ya existe, get_or_create() la recupera de la base de datos y si no existe, la crea en ese instante.

**Verificación:** (.venv) ➜  examen2-topicos-avanzados-o26 git:(main) ✗ python manage.py cargar_datos
Socios: 40
Clases: 20
Carga terminada

**Commit:** el mensaje del commit de esta corrección.

## Falla 1 (Parte 1 / Ticket N / F1 / F2 / Extra)

**Síntoma:** RuntimeError: Model class gimnasio.models.Disciplina doesn't declare an explicit app_label and isn't in an application in INSTALLED_APPS


**Causa raíz:** Django está intentando cargar tu modelo Disciplina pero no esta la app agregada en las installed apps en tu archivo de settings.py.

**Corrección:** en settings.py añadí en INSTALLED_APPS debajo de rest_framework: , gimasio

**Verificación:** python manage.py migrate, todas las migraciones ok

**Commit:** el mensaje del commit de esta corrección.

---
## Falla 3 (Parte 2 / Ticket 1 / F1 / F2 / Extra)

**Síntoma:** Reverse for 'detalle_clase' not found. 'detalle_clase' is not a valid view function or pattern name.


**Causa raíz:** En en gimnasio/urls.py está escrito:     path("clases/<int:pk>/", views.clase_detalle, name="clase_detalle") y está buscando detalle_clase

**Corrección:** corregir en name="detalle_clase"

**Verificación:** tenía mi servidor corriendo, solo de di refresh y ya sale la tabla con las clases de la semana.

**Commit:** el mensaje del commit de esta corrección.

---
## Falla 4 (Parte 2 / Ticket 2 / F1 / F2 / Extra)

**Síntoma:** Las clases en ?con_lugar=1 salían aun cuando estaban o completas o canceladas


**Causa raíz:** en models.py, la calse ClaseQuerrySet en la funcon con_lugar solo contaba con filtrar las clases por num_inscritos__lte=F("cupo"). 

**Corrección:** pegué en google qué hace __lte y es less or equal, entonces las  iba a mostrar aun estando 20/20, entonces se corrige con __lt para que sea < y también se filtra unicamente si la clase tiene el estado de ACTIVA, pues antes no hacia ese filtro 

**Verificación:** refresh, darle en el dashboard a ver solo clases con lugar y ya sale la busqueda con el filtro bien

**Commit:** el mensaje del commit de esta corrección.

---





## Declaración de uso de IA

Marca una opción.

- [ ] No usé asistentes de IA en este examen.
- [ ] Sí usé asistentes de IA. Para cada uso: herramienta, qué le pedí, qué usé de su respuesta y qué revisé o cambié yo.
