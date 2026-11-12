"""Pruebas del hash de contraseñas (requieren bcrypt instalado)."""

import re
import unittest

try:
    from vepo.services.security import hash_password, verify_password
except ModuleNotFoundError:  # bcrypt no instalado
    hash_password = None


@unittest.skipIf(hash_password is None, "bcrypt no está instalado")
class SecurityTest(unittest.TestCase):
    def test_hash_matches_database_check(self):
        hashed = hash_password("Prueba#2026")
        self.assertRegex(hashed, re.compile(r"^\$2[abxy]\$[0-9]{2}\$.{53}$"))

    def test_verify(self):
        hashed = hash_password("Prueba#2026")
        self.assertTrue(verify_password("Prueba#2026", hashed))
        self.assertFalse(verify_password("otra-clave", hashed))
        self.assertFalse(verify_password("x", "no-es-un-hash"))

    def test_short_password_rejected(self):
        with self.assertRaises(ValueError):
            hash_password("corta")


if __name__ == "__main__":
    unittest.main()
