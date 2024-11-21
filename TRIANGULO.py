A=float(input("Ingrese el valor del lado A del triangulo:"))
B=float(input("Ingrese el valor del lado B del triangulo:"))
C=float(input("Ingrese el valir del lado C del triangulo:"))
if A+B>C and A+C>B and B+C>A :
    if A==B==C:
        print("Es un triangulo equilatero")
    elif A !=B and B !=C and C !=A:
        print("Es un triangulo escaleno")
    else:
        print("Los lados invgresados no forman un triangulo")
