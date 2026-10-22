import csv
from datetime import date, time
from pathlib import Path

from django.conf import settings
from django.core.management.base import BaseCommand

from gimnasio.models import Clase, Disciplina, Socio


def leer_csv(nombre):
    ruta = Path(settings.BASE_DIR) / "data" / nombre
    with open(ruta, encoding="utf-8", newline="") as archivo:
        return list(csv.DictReader(archivo))


class Command(BaseCommand):
    help = "Carga socios, clases e inscripciones desde la carpeta data/"

    def handle(self, *args, **options):
        # 1. Socios
        for fila in leer_csv("socios.csv"):
            Socio.objects.update_or_create(
                numero=fila["numero"],
                defaults={
                    "nombre": fila["nombre"],
                    "correo": fila["correo"],
                    "vence_membresia": date.fromisoformat(fila["vence_membresia"]),
                },
            )
        self.stdout.write(f"Socios: {Socio.objects.count()}")

        # 2. Clases
        for fila in leer_csv("clases.csv"):
            disciplina, _ = Disciplina.objects.get_or_create(nombre=fila["disciplina"])
            Clase.objects.update_or_create(
                codigo=fila["codigo"],
                defaults={
                    "disciplina": disciplina,
                    "instructor": fila["instructor"],
                    "dia": fila["dia"],
                    "hora": time.fromisoformat(fila["hora"]),
                    "cupo": int(fila["cupo"]),
                    "estado": fila["estado"],
                    "sala": fila["sala"],
                },
            )
        self.stdout.write(f"Clases: {Clase.objects.count()}")

        # 3. Inscripciones
        for fila in leer_csv("inscripciones.csv"):
            clase = Clase.objects.get(codigo=fila["clase"])
            socio = Socio.objects.get(numero=fila["socio"])
            clase.inscritos.add(socio)
        self.stdout.write(self.style.SUCCESS("Carga terminada"))
