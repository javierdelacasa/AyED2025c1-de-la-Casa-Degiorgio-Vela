import unittest
import random
from burbuja import burbuja
from quicksort import ordenamientoRapido
from radixsort import radix_sort


class Test_Burbuja(unittest.TestCase):
    
    def test_burbuja(self):
        for n in range(500):  # Hacemos 500 pruebas distintas
            with self.subTest(i=n):
                lista = [random.randint(10000, 99999) for _ in range(500)]
                lista_copia = lista.copy()

                burbuja(lista)
                resultado_burbuja = lista
                resultado_correcto = sorted(lista_copia)

                self.assertEqual(resultado_burbuja, resultado_correcto)

class Test_quicksort(unittest.TestCase):
    
    def test_quicksort(self):
        for n in range(500):
            with self.subTest(i=n):
                lista = [random.randint(10000, 99999) for _ in range(500)]
                lista_copia = lista.copy()

                ordenamientoRapido(lista)
                resultado_quick = lista
                resultado_correcto = sorted(lista_copia)

                self.assertEqual(resultado_quick, resultado_correcto)

class Test_radixsor(unittest.TestCase):
    
    def test_radixsort(self):
        for n in range(500):
            with self.subTest(i=n):
                lista = [random.randint(10000, 99999) for _ in range(500)]
                lista_copia = lista.copy()

                radix_sort(lista)
                resultado_radix= lista
                resultado_correcto = sorted(lista_copia)

                self.assertEqual(resultado_radix, resultado_correcto)

if __name__ == "__main__":
    unittest.main()