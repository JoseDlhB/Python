import unittest

from sqlalchemy import false, true

"""
- Se basan en el flujo del program
- Prueba todos los caminos posibles de una función.
  Ramificaciones, bucles for y while, reursión.
- Regression testing o mocks.
"""

def es_mayor_edad(edad):
    if edad >= 18:
        return True
    else:
        return False


class PrubaDeCristalTest(unittest.TestCase):
    def test_es_mayor_edad(self):
        edad = 20

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, True)

    def test_es_menor_edad(self):
        edad = 15

        resultado = es_mayor_edad(edad)

        self.assertEqual(resultado, False)


if __name__ == '__main__':
    unittest.main()

