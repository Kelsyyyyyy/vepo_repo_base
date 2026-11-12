"""Validaciones de reglas de negocio (RN) sin dependencias externas."""

import re
from datetime import date
from decimal import Decimal

_USERNAME_RE = re.compile(r"^[a-z0-9._-]{4,30}$")


def validate_amount(amount: Decimal) -> Decimal:
    """Comprueba que un monto sea mayor que cero (RN-03).

    Args:
        amount: monto en pesos de la venta o del egreso.

    Returns:
        El mismo monto, si es válido.

    Raises:
        ValueError: si el monto es cero o negativo.
    """
    if amount <= 0:
        raise ValueError("El monto debe ser mayor que 0.")
    return amount


def validate_username(username: str) -> str:
    """Comprueba el formato del usuario (RN-12).

    Args:
        username: texto escrito por la persona.

    Returns:
        El usuario sin espacios en los extremos.

    Raises:
        ValueError: si no tiene 4 a 30 caracteres entre minúsculas,
            números, punto, guion o guion bajo.
    """
    clean = username.strip()
    if not _USERNAME_RE.fullmatch(clean):
        raise ValueError("Usuario no válido: 4 a 30 caracteres [a-z0-9._-].")
    return clean


def validate_period(date_start: date, date_finish: date) -> None:
    """Comprueba que el inicio del corte no sea posterior al fin (RN-09).

    Args:
        date_start: primer día de la quincena.
        date_finish: último día de la quincena.

    Raises:
        ValueError: si ``date_start`` es posterior a ``date_finish``.
    """
    if date_start > date_finish:
        raise ValueError("La fecha de inicio no puede ser posterior a la de fin.")


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
