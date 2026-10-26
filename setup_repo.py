from pathlib import Path


ROOT = Path(__file__).resolve().parent

DIRECTORIES = [
    "01_fundamentos/01_variables_y_tipos",
    "01_fundamentos/02_condicionales",
    "01_fundamentos/03_ciclos_y_listas",
    "01_fundamentos/04_funciones",
    "02_estructuras_datos/01_diccionarios_sets",
    "02_estructuras_datos/02_archivos_csv_json",
    "03_analisis_datos/datasets",
    "03_analisis_datos/01_pandas_basico",
    "04_sql/esquemas",
    "04_sql/consultas",
]

GITIGNORE_CONTENT = """__pycache__/
*.pyc

.env

.pytest_cache/

.venv/
venv/

.DS_Store
"""

README_CONTENT = """# Python & Data Lab

Repositorio de práctica progresiva que documenta el aprendizaje desde los fundamentos de programación en Python hasta el análisis de datos, la ingeniería de datos y las consultas SQL.

## Hoja de ruta

| Fase | Módulo | Contenido |
|---|---|---|
| Fase 1 | Fundamentos | Variables, tipos de datos, condicionales, ciclos, listas y funciones |
| Fase 2 | Estructuras | Diccionarios, conjuntos, archivos CSV y JSON |
| Fase 3 | Análisis de Datos | Datasets y fundamentos de análisis con pandas |
| Fase 4 | Consultas SQL | Esquemas, consultas y fundamentos de SQL |

## Estructura principal

- `01_fundamentos/`: conceptos esenciales de programación con Python.
- `02_estructuras_datos/`: estructuras de datos y manejo de archivos.
- `03_analisis_datos/`: datasets y análisis exploratorio con pandas.
- `04_sql/`: esquemas y consultas SQL.

## Guía de commits

Se recomienda utilizar mensajes de commit semánticos:

- `feat:` para agregar una funcionalidad o contenido nuevo.
- `docs:` para modificar documentación.
- `refactor:` para reorganizar o mejorar código sin cambiar su comportamiento.
- `test:` para agregar o modificar pruebas.

Ejemplos:

```text
feat: agregar práctica de diccionarios
docs: actualizar hoja de ruta
refactor: reorganizar ejemplos de funciones
test: agregar pruebas para validación de datos
```

## Requisitos mínimos

- Python 3.10 o superior.
- Git.
"""


def create_structure() -> None:
    for directory in DIRECTORIES:
        directory_path = ROOT / directory
        directory_path.mkdir(parents=True, exist_ok=True)

        gitkeep_path = directory_path / ".gitkeep"
        gitkeep_path.touch(exist_ok=True)


def create_root_files() -> None:
    (ROOT / ".gitignore").write_text(
        GITIGNORE_CONTENT,
        encoding="utf-8",
    )
    (ROOT / "README.md").write_text(
        README_CONTENT,
        encoding="utf-8",
    )


def main() -> None:
    create_structure()
    create_root_files()
    print("Estructura base de python-data-lab creada correctamente.")


if __name__ == "__main__":
    main()
