# VEPO · Control operativo de la purificadora

Sistema de escritorio (Python + tkinter + PostgreSQL) para registrar ventas,
parámetros de calidad del agua, egresos y cortes quincenales de
**Agua Inmaculada, sucursal Porfirio Díaz**. Proyecto Integrador I · UTD.

## Requisitos
Windows 10/11 · Python 3.12 (con tcl/tk) · PostgreSQL 18 · Git · DBeaver (opcional).

## Instalación rápida
```powershell
git clone <URL-del-repositorio> vepo
cd vepo
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
copy .env.example .env      # edita usuario y contraseña
pre-commit install
```

Base de datos: crear la base `vepo` y ejecutar en orden `db/01_ddl.sql`,
`db/02_dml.sql`, `db/03_consultas.sql` y `db/04_seguridad.sql`.

## Ejecutar y probar
```powershell
python -m vepo
python -m unittest discover -s tests -v
ruff check . ; ruff format --check .
```

## Estructura
`src/vepo/` (models, views, controllers, services, utils) · `db/` · `tests/` ·
`docs/` · `portafolio/`. Arquitectura MVC: ver `docs/arquitectura/`.

## Equipo y reglas
Equipo VEPO · Docente: Raúl Iván Herrera González.
Antes de colaborar lee [CONTRIBUTING.md](CONTRIBUTING.md).
## Responsable y fecha
Responsable del repositorio: Kelsy Diez.
Última actualización: 12 de noviembre de 2026.
