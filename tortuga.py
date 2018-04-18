import turtle


def aplicarProducciones(palabra):

    nuevaPalabra = ""
    for simbolo in palabra:
        nuevaPalabra = nuevaPalabra + aplicarRegla(simbolo)

    return nuevaPalabra

def aplicarRegla(simbolo):

    if simbolo == "f":
        return "f+f-f-f++"
    elif simbolo == "b":
        return "b-"


def dibujar(turtle, cadena):
    for c in cadena:
        if c == 'f':
            turtle.forward(5)
        elif c == 'b':
            turtle.backward(5)
        elif c == '+':
            turtle.right(60)
        elif c == '-':
            turtle.left(60)


palabraInicial = "f"
vueltas = 10
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
