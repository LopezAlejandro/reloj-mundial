import datetime

def ver_hora(zona_horaria):
    formato="%H:%M:%S"
    if zona_horaria == -3:
        zona = "Hora Bs As"
    elif zona_horaria == -5:
        zona = "Hora de New York"
    else :
        zona = "Hora de San Francisco"

    time_zone=datetime.timezone(datetime.timedelta(hours=zona_horaria))
    hora_actual=datetime.datetime.now(time_zone).time()

    print("La hora exacta es : {} {}".format( hora_actual.strftime(formato),zona))

def ver_fecha_hora():
    formato="%B %d,%Y  %H:%M:%S"
    time_zone=datetime.timezone(datetime.timedelta(hours=-3))
    fecha_actual=datetime.datetime.now(time_zone)
    print("La fecha es : {}".format( fecha_actual.strftime(formato)))

def ver_instruciones():

    print("Estas son las operaciones que puedes realizar")
    print("1 - Para ver la hora")
    print("2 - Para ver la fecha y hora")
    print("3 - para ver la hora en New York")
    print("4 - Para ver la hora en San Francisco")
    print("5 - para ver las instrucciones")
    print("6 - Para salir")

def ver_reloj():
    print("Bienvenido al reloj del mundo")
    ver_instruciones()

    while True:
        operacion = input(" : ")

        if (operacion == "1"):
            ver_hora(-3)
        elif operacion =="2":
            ver_fecha_hora()
        elif operacion == "3":
            ver_hora(-5)
        elif operacion=="4":
            ver_hora(-8)
        elif operacion =="5":
            ver_instruciones()
        elif operacion == "6":
            break
        else:
            print("No conozco esa operacion")
    print("Gracias por usar el reloj mundial")

ver_reloj()
