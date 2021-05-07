def areaCuadrado():
  print("1.Cuadrado")
  lado=int(input("captura el lado:"))
  area=lado*lado
  print("El area es:"+str(area))
  perimetro=lado*4
  print("El parametro es:"+str(perimetro))


def areaTriangulo():
  print("2.Triangulo")
  base=int(input("Captura la base:"))
  altura=int(input("Captura el area:"))
  a=(base*altura)/2
  print("El area es:"+str(a))
  perimetro=base*3
  
  print("El area es:"+str(perimetro))

print("calcula area y perimetro")

def areaRectangulo():
  print("3.Rectangulo")
  base=int(input("Captura la base:"))
  altura=int(input("Captura el area:"))
  a=(base*altura)/2
  print("El area es:"+str(a))
  perimetro=base*4
  
  print("El area es:"+str(perimetro))

print("opciones:")
print("1.Cuadrado")
print("2.Triangulo")
print("3.Rectangulo")


numero=int(input("Ingresar el numero de la operacion a elegir:"))

if numero==1:
  areaCuadrado()
elif numero==2:
  areaTriangulo()
elif numero==3:
  areaRectangulo()