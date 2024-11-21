bonificacion=float(input("Ingrese el valo de su bonificacion"))
if bonificacion<50000 :
    print(f"Compre una camara web ya que su bonificacion es de:{bonificacion}")
elif bonificacion>=50000 and bonificacion<=200000 :
    print (f"Compre un subwoofer ya que su bonificacion es de: {bonificacion}")
elif bonificacion>=200000 and bonificacion<=500000 :
    print(f"Compre un DD extremo ya que su bonificacion es de: {bonificacion}")
elif bonificacion>=500000 and bonificacion<=1000000 :
    print (f"Compre una impresora multifuncional ya que su bonificacion es de:{bonificacion}")
elif bonificacion>=1000000 :
    print (f"Compre un proyector ya que su bonificacion es de:{bonificacion}")
       