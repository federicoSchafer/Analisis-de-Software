def esTriangulo(l1, l2, l3):
	if type(l1) == int and type(l2) == int and type(l3) == int:
		return (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1
	else:
		return False

def esEquilatero(l1, l2, l3):
	return l1 == l2 == l3

def esIsoceles(l1, l2, l3):
	return (l1 == l2 and l1 != l3) or (l1 == l3 and l1 != l2) or (l2 == l3 and l3 != l1)

def esEscaleno(l1, l2, l3):
	return l1 != l2 != l3 and l1 != l3

def clasificacionTriangulo(*lado):
	cantLados = 0
	for i in lado:
		cantLados += 1
	if cantLados != 3:
		return "No es un Triangulo"
	l1 = lado[0]
	l2 = lado[1]
	l3 = lado[2]
	if not esTriangulo(l1, l2, l3):
		return "No es un Triangulo"
	if esEquilatero(l1, l2, l3):
		return "Es un triangulo Equilatero"
	if esIsoceles(l1, l2, l3):
		return "Es un triangulo Isoceles"
	return "Es un triangulo Escaleno"