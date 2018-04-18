
import math
import bpy

orientacion = [0,1,0]
pos = [0,0,0]



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



def makePoly(cadena):

    global orientacion
    global pos
    global verts
    for c in cadena:

        if c == 'f':
            v = [pos[0] + orientacion[0],pos[1] + orientacion[1],0]
            pos = v
            verts.append(v)

        elif c == '+':
            dirX = orientacion[0]
            dirY = orientacion[1]
            if dirX == 0 and dirY == 0:
                orientacion = [0,1,0]

            elif dirX == 0 and dirY == 1:
                orientacion = [1,1,0]

            elif dirX == 1 and dirY == 0:
                orientacion = [-1,1,0]

            elif dirX == 1 and dirY == 1:
                orientacion = [1,0,0]

            elif dirX == 0 and dirY == -1:
                orientacion = [-1,-1,0]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,1,0]

            elif dirX == -1 and dirY == -1:
                orientacion = [-1,0,0]


        elif c == '-':
            dirX = orientacion[0]
            dirY = orientacion[1]
            if dirX == 0 and dirY == 0:
                orientacion = [0,-1,0]

            elif dirX == 0 and dirY == 1:
                orientacion = [-1,1,0]

            elif dirX == 1 and dirY == 0:
                orientacion = [1,1,0]

            elif dirX == 1 and dirY == 1:
                orientacion = [0,1,0]

            elif dirX == 0 and dirY == -1:
                orientacion = [1,-1,0]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,-1,0]

            elif dirX == -1 and dirY == -1:
                orientacion = [0,-1,0]




verts=[]

faces = []

palabraInicial = "f"
vueltas = 10
palabra = ""
for i in range(vueltas):
    palabra = palabra + aplicarProducciones(palabraInicial)

makePoly(palabra)

mesh = bpy.data.meshes.new("test");
mesh.from_pydata(verts, [], faces)
mesh.validate(True)
mesh.show_normal_face = True

obj = bpy.data.objects.new("test", mesh)
scn = bpy.context.scene
scn.objects.link(obj)
