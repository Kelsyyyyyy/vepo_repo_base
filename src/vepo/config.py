"""Lectura de la configuración desde variables de entorno (archivo .env)."""

import os

from dotenv import load_dotenv

load_dotenv()


def get_db_settings() -> dict[str, str]:
    """Devuelve los datos de conexión a PostgreSQL.

    Returns:
        Diccionario con host, port, dbname, user y password.

    Raises:
        KeyError: si falta VEPO_DB_USER o VEPO_DB_PASSWORD en el entorno.
    """
    return {
        "host": os.environ.get("VEPO_DB_HOST", "localhost"),
        "port": os.environ.get("VEPO_DB_PORT", "5432"),
        "dbname": os.environ.get("VEPO_DB_NAME", "vepo"),
        "user": os.environ["VEPO_DB_USER"],
        "password": os.environ["VEPO_DB_PASSWORD"],
    }
