import turtle


def aplicarProducciones(palabra):

    nuevaPalabra = ""
    for simbolo in palabra:
        nuevaPalabra = nuevaPalabra + aplicarRegla(simbolo)

    return nuevaPalabra

def aplicarRegla(simbolo):

    if simbolo == "f":
        return "fffff+ff-f+"
    elif simbolo == "b":
        return "b-"


def dibujar(turtle, cadena):
    for c in cadena:
        if c == 'f':
            turtle.forward(5)
        elif c == 'b':
            turtle.backward(5)
        elif c == '+':
            turtle.right(45)
        elif c == '-':
            turtle.left(45)


palabraInicial = "f"
vueltas = 8
palabra = ""
for i in range(vueltas):
    palabra = palabra + aplicarProducciones(palabraInicial)

tortuga = turtle.Turtle()
pantalla = turtle.Screen()
print palabra

tortuga.up()
tortuga.back(200)
tortuga.down()
tortuga.speed(9)
dibujar(tortuga, palabra)
pantalla.exitonclick()
