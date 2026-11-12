"""Hash y verificación de contraseñas con bcrypt (RN-02)."""

import bcrypt

BCRYPT_COST = 12
MIN_PASSWORD_LENGTH = 8


def hash_password(plain: str) -> str:
    """Genera el hash bcrypt de una contraseña.

    Args:
        plain: contraseña en texto plano (mínimo 8 caracteres).

    Returns:
        Hash bcrypt de 60 caracteres, listo para guardar en logeo.password.

    Raises:
        ValueError: si la contraseña es demasiado corta.
    """
    if len(plain) < MIN_PASSWORD_LENGTH:
        raise ValueError("La contraseña debe tener al menos 8 caracteres.")
    salt = bcrypt.gensalt(rounds=BCRYPT_COST)
    return bcrypt.hashpw(plain.encode("utf-8"), salt).decode("ascii")


def verify_password(plain: str, hashed: str) -> bool:
    """Compara una contraseña escrita con el hash guardado.

    Args:
        plain: contraseña escrita al iniciar sesión.
        hashed: hash bcrypt guardado en la base de datos.

    Returns:
        True si coinciden; False en cualquier otro caso.
    """
    try:
        return bcrypt.checkpw(plain.encode("utf-8"), hashed.encode("ascii"))
    except ValueError:
        return False
