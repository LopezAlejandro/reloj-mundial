import datetime

print ("Bienvenido al reloj del mundo")
print ("Estas son las operaciones que puedes realizar")
print ("1 - Para ver la hora")
print ("2 - Para ver la fecha y hora")
print ("3 - para ver la hora en New York")
print ("4 - Para ver la hora en San Francisco")
print ("5 - para ver las instrucciones")
print ("6 - Para salir")

while True:
    operacion = input(" : ")

    if (operacion == "1"):
        print (datetime.datetime.now().time())
    elif operacion =="2":
        print (datetime.datetime.now())
    elif operacion == "3":
        print ("Hora en Nueva York")
    elif operacion=="4":
        print ("Hora en San Francisco")
    elif operacion =="5":
        print ("Ver instrucciones")
    elif operacion == "6":
        break
    else:
        print("No conozco esa operacion")
