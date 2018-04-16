import unittest
import Triangulo

class TestTriangulo(unittest.TestCase):

	def test_noTrianguloSumaPrimerosIgualTercero(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(1,2,3), "No es un Triangulo")

	def test_noTrianguloSumaPrimerosIgualTerceroPermutando(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(2,1,3), "No es un Triangulo")

	def test_noTrianguloSumaPrimerosMenorTerecero(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(2,1,5), "No es un Triangulo")

	def test_noTrianguloSumaPrimerosMenorTereceroPermutando(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(1,2,6), "No es un Triangulo")

	def test_equilateroValido(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(2,2,2),"Es un triangulo Equilatero")

	def test_isocelesValido(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(2,2,3), "Es un triangulo Isoceles")
	
	def test_isocelesPermutado1(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(2,3,2), "Es un triangulo Isoceles")

	def test_isocelesPermutado2(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(3,2,2), "Es un triangulo Isoceles")

	def test_escalenoValido(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(4,3,5), "Es un triangulo Escaleno")

	def test_entradaNegativa(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(-1,-4,-10), "No es un Triangulo")

	def test_entradaChar(self):
		self.assertEqual(Triangulo.clasificacionTriangulo('A',3,5), "No es un Triangulo")

	def test_entradaString(self):
		self.assertEqual(Triangulo.clasificacionTriangulo("Hola", "soy", "String"), "No es un Triangulo")

	def test_entradaFloat(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(3.14, 2.17, "HOLA"), "No es un Triangulo")

	def test_entradaEspecial(self):
		self.assertEqual(Triangulo.clasificacionTriangulo('!','$','%'), "No es un Triangulo")

	def test_entradaCeros(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(0,0,0), "No es un Triangulo")

	def test_unaEntradaCon0(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(0,4,5), "No es un Triangulo")

	def test_entradaMal(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(3,3), "No es un Triangulo")

	def test_entradaMal2(self):
		self.assertEqual(Triangulo.clasificacionTriangulo(3,3,4,5), "No es un Triangulo")

if __name__ == "__main__":
    unittest.main()
