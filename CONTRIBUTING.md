# Guía de contribución · Proyecto VEPO

Esta guía la sigue **todo el equipo**. Si algo no está aquí, se propone en un PR
a este mismo archivo. Stack: Python 3.12 · tkinter/ttk · PostgreSQL 18 ·
arquitectura MVC · Git y GitHub.

## 1. Flujo de trabajo en Git

**Ramas**

| Rama | Para qué | Reglas |
| --- | --- | --- |
| `main` | Versión estable que se entrega o instala en la sucursal | Protegida. Solo recibe PR desde `develop` al cerrar un sprint |
| `develop` | Integración del trabajo del sprint | Protegida. Solo recibe PR desde ramas de trabajo |
| `feature/HU-xx-descripcion-corta` | Una historia de usuario | Sale de `develop`. Vida corta (1 a 3 días) |
| `fix/descripcion-corta` | Corrección de un error | Sale de `develop` |
| `docs/descripcion-corta` | Solo documentación | Sale de `develop` |

Ejemplos: `feature/HU-03-venta-ruta`, `fix/validar-fecha-corte`.

**Commits (Conventional Commits, en español, modo imperativo)**

```
<tipo>: <qué se hizo> (HU-xx)
```

Tipos: `feat` (funcionalidad) · `fix` (error) · `docs` · `style` (formato, sin
cambiar lógica) · `refactor` · `test` · `chore` (configuración, dependencias).

Ejemplos: `feat: registrar venta de ruta (HU-03)` · `fix: validar fecha de
corte (HU-06)` · `docs: agregar diagrama de red`.

**Pull request (PR)**

1. Nadie hace *push* directo a `main` ni a `develop`.
2. Cada PR lleva la plantilla completa (se carga sola) y enlaza la HU.
3. Necesita **1 aprobación de otra persona** del equipo (no la autora) y que el
   CI (`ruff` + pruebas) esté en verde.
4. Se hace *squash and merge* y se borra la rama.
5. Quien revisa comprueba la Definición de Terminado técnica (sección 6),
   deja comentarios concretos y no aprueba lo que no puede explicar.

## 2. Arquitectura MVC (qué va dónde)

| Carpeta | Contiene | No debe contener |
| --- | --- | --- |
| `src/vepo/views/` | Ventanas y widgets tkinter/ttk. Solo muestran datos y avisan eventos | SQL, reglas de negocio |
| `src/vepo/controllers/` | Reciben eventos de la vista, validan permisos por rol, llaman al modelo y devuelven el resultado | Widgets, SQL |
| `src/vepo/models/` | Clases del dominio (Sale, Employee…) y acceso a datos (consultas parametrizadas) | tkinter |
| `src/vepo/services/` | Seguridad (bcrypt), sesión, respaldos | tkinter |
| `src/vepo/utils/` | Funciones puras y validadores (reglas RN) | Acceso a la base de datos |

## 3. Nomenclatura y formato

- Identificadores **en inglés** (igual que la base de datos); textos que ve la
  persona usuaria **en español**.
- Archivos, funciones y variables: `snake_case`. Clases: `PascalCase`.
  Constantes: `MAYUSCULAS_CON_GUION_BAJO`. Privados: prefijo `_`.
- Indentación: 4 espacios (nunca tabuladores). Línea máxima: 88 caracteres.
- Comillas dobles. Imports ordenados (lo hace `ruff`).
- Funciones de máximo ~30 líneas y una sola responsabilidad. Con anotaciones de
  tipo en parámetros y retorno.
- Nada de números mágicos: usa constantes con nombre (`BCRYPT_COST = 12`).
- El formato lo aplica `ruff format` al guardar y en `pre-commit`; no se discute
  a mano.

## 4. Comentarios y docstrings

Toda función, clase y módulo público lleva docstring estilo Google
(`Args`, `Returns`, `Raises`). Los comentarios `#` explican el **porqué**, no
repiten el código. Se cita la regla de negocio cuando aplica (RN-xx).

```python
def calculate_closing_total(amount_window: Decimal, amount_route: Decimal) -> Decimal:
    """Calcula el total del corte: ventana + ruta (RN-08).

    Args:
        amount_window: total de ventas de ventana del periodo (>= 0).
        amount_route: total de ventas de ruta del periodo (>= 0).

    Returns:
        Total general del corte.

    Raises:
        ValueError: si alguno de los montos es negativo.
    """
    if amount_window < 0 or amount_route < 0:
        raise ValueError("Los totales del corte no pueden ser negativos.")
    return amount_window + amount_route
```

## 5. Reglas de seguridad al programar

- **Siempre** consultas parametrizadas: `cur.execute("... WHERE x = %s", (x,))`.
  Prohibido armar SQL con f-strings o `+`.
- Contraseñas solo como hash bcrypt (`services/security.py`). Nunca en texto,
  logs ni pantallas.
- La aplicación se conecta como `app_vepo`, nunca como `postgres`.
- Credenciales en `.env` (ignorado por Git). Si una clave se sube por error, se
  avisa al líder y se cambia de inmediato.
- Los permisos por rol se validan en el **controlador**, no solo ocultando
  botones.
- Mensajes de error al usuario sin detalles técnicos ni datos sensibles.

## 6. Definición de Terminado técnica

Una tarea está terminada cuando:

1. `ruff check .` y `ruff format --check .` pasan sin errores.
2. Las funciones públicas tienen docstring con `Args`, `Returns` y `Raises`.
3. Tiene prueba (`tests/`) y `python -m unittest discover -s tests` pasa.
4. Respeta MVC (sección 2) y las reglas de seguridad (sección 5).
5. La pantalla sigue la guía de estilo de A10 (colores, contraste, mensajes).
6. Fue revisada y aprobada por otra persona en un PR y el CI está en verde.
7. README o `docs/` actualizados si cambió la instalación o el uso.

## 7. Estructura de carpetas

```
vepo/
├─ .github/            plantilla de PR y CI
├─ db/                 01_ddl.sql · 02_dml.sql · 03_consultas.sql · 04_seguridad.sql
├─ docs/               arquitectura/ · interfaz/
├─ portafolio/         A08 ... A11 (entregables en PDF)
├─ src/vepo/           models/ · views/ · controllers/ · services/ · utils/
├─ tests/
├─ CONTRIBUTING.md · README.md · pyproject.toml · requirements*.txt · .env.example
```

## 8. Plantilla de README para módulos o documentos nuevos

Título · Qué hace (1 párrafo) · Requisitos · Instalación · Uso (con ejemplo) ·
Pruebas · Responsable y fecha de la última actualización.

## 9. Configuración inicial (cada integrante)

```powershell
py -3.12 -m venv .venv
.venv\Scripts\activate
pip install -r requirements-dev.txt
pip install -e .
pre-commit install
```

## 10. Uso de IA

Si se usa un asistente de IA para programar o documentar, se declara en la
tabla de herramientas del documento A11 y en el PR (qué se pidió y qué se
cambió). Nadie entrega código o configuración que no pueda explicar.
