"""Conexión a PostgreSQL. Todas las consultas se parametrizan con %s."""

import psycopg

from vepo.config import get_db_settings


def get_connection() -> psycopg.Connection:
    """Abre una conexión con el usuario de la aplicación (app_vepo).

    Returns:
        Conexión activa a la base de datos ``vepo``.

    Raises:
        psycopg.OperationalError: si el servidor no responde o las
            credenciales son incorrectas.
    """
    cfg = get_db_settings()
    return psycopg.connect(
        host=cfg["host"],
        port=cfg["port"],
        dbname=cfg["dbname"],
        user=cfg["user"],
        password=cfg["password"],
        options="-c search_path=agua_inmaculada",
    )
