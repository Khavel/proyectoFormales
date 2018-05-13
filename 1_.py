
import bpy
import random
from math import *

def aplicarProducciones(palabra):

    nuevaPalabra = ""
    for simbolo in palabra:
        nuevaPalabra = nuevaPalabra + aplicarRegla(simbolo)

    return nuevaPalabra

def aplicarRegla(simbolo):
    if simbolo == "f":
        rand = random.randrange(1, 5)
        if rand == 1.0:
            return "*f[+f[++f-f][-f+f]][-f[-f+f][+f-f]]ff"
        elif rand == 2.0:
            return "+*f[+f[++f-f][-f+f]][-f]fff"
        elif rand == 3.0:
            return "fff--f[++f-f]/"
        elif rand == 4.0:
            return "*f[+f[-f+f]][+f-f]fff"
        elif rand == 5.0:
            return "*f[++f-f]++"
    else:
        return simbolo



def makePoly(cadena):
    step = 0.5
    stepV = 0.4
    orientacion = [step,step,stepV]
    pos = [0,0,0]
    brackets = []
    ant = 0
    vertCont = 0
    trasBracket = False
    posPre = []
    cAnt = 'x'

    for c in cadena:

        if c == 'f':
            v = [pos[0] + orientacion[0],pos[1] + orientacion[1],pos[2] + orientacion[2]]
            pos = v
            if not v in verts:
                verts.append(v)
                vertCont = vertCont + 1
                if not trasBracket:
                    edges.append((vertCont-1,vertCont-2))
                else:
                    trasBracket = False
                    edges.append((vertCont-1,ant))

        #Guarda la posicion
        elif c == '[':
            brackets.append((pos,orientacion))
            if not cAnt == ']':
                posPre.append(vertCont-1)
            else:
                posPre.append(ant)
            raices.append(vertCont-1)


        #Retorna a la ultima posicion guardada
        elif c == ']':
            pos_brackets,head_brackets = brackets.pop()
            pos = pos_brackets
            orientacion = head_brackets
            trasBracket = True
            ant = posPre.pop()
            vverts.append(vertCont-1)


        elif c == '+':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]
            if dirX == 0 and dirY == step:
                orientacion = [step,step,dirZ]

            elif dirX == step and dirY == step:
                orientacion = [step,0,dirZ]

            elif dirX == step and dirY == 0:
                orientacion = [step,-step,dirZ]

            elif dirX == step and dirY == -step:
                orientacion = [0,-step,dirZ]

            elif dirX == 0 and dirY == -step:
                orientacion = [-step,-step,dirZ]

            elif dirX == -step and dirY == -step:
                orientacion = [-step,0,dirZ]

            elif dirX == -step and dirY == 0:
                orientacion = [-step,step,dirZ]

            elif dirX == -step and dirY == step:
                orientacion = [0,step,dirZ]


        elif c == '-':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirX == 0 and dirY == step:
                orientacion = [-step,step,dirZ]

            elif dirX == step and dirY == step:
                orientacion = [0,step,dirZ]

            elif dirX == step and dirY == 0:
                orientacion = [step,step,dirZ]

            elif dirX == step and dirY == -step:
                orientacion = [step,0,dirZ]

            elif dirX == 0 and dirY == -step:
                orientacion = [step,-step,dirZ]

            elif dirX == -step and dirY == -step:
                orientacion = [0,-step,dirZ]

            elif dirX == -step and dirY == 0:
                orientacion = [-step,-step,dirZ]

            elif dirX == -step and dirY == step:
                orientacion = [-step,0,dirZ]

            #Hacia arriba
        elif c == '*':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirZ == 0:
                orientacion = [dirX,dirY,stepV]

            elif dirZ == stepV:
                v = [pos[0],pos[1],pos[2] + stepV]
                pos = v
                if not v in verts:
                    verts.append(v)
                    vertCont = vertCont + 1
                    if not trasBracket:
                        edges.append((vertCont-1,vertCont-2))
                    else:
                        trasBracket = False
                        edges.append((vertCont-1,ant))

            elif dirZ == -stepV:
                orientacion = [dirX,dirY,0]
            #Hacia abajo
        elif c == '/':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirZ == 0:
                orientacion = [dirX,dirY,-stepV]

            elif dirZ == stepV:
                orientacion = [dirX,dirY,0]

            elif dirZ == -stepV:
                v = [pos[0],pos[1],pos[2] - stepV]
                pos = v
                if not v in verts:
                    verts.append(v)
                    vertCont = vertCont + 1
                    if not trasBracket:
                        edges.append((vertCont-1,vertCont-2))
                    else:
                        trasBracket = False
                        edges.append((vertCont-1,ant))
        cAnt = c

def measure (first, second):
	locx = second[0] - first[0]
	locy = second[1] - first[1]
	locz = second[2] - first[2]
	distance = sqrt((locx)**2 + (locy)**2 + (locz)**2)
	return distance


verts=[]
edges = []
faces = []
vverts = []
raices = []

vueltas = 5
palabra = "f"
for i in range(vueltas):
    palabra = palabra + aplicarProducciones(palabra)


makePoly(palabra)



mesh = bpy.data.meshes.new("test");
mesh.from_pydata(verts, edges, faces)
mesh.validate(True)
mesh.show_normal_face = True

obj = bpy.data.objects.new("test", mesh)

for i,v in enumerate(verts):
    vg = obj.vertex_groups.new(name=str(i))
    vg.add([i],1.0, 'ADD')
scn = bpy.context.scene
scn.objects.link(obj)

bpy.context.scene.objects.active = obj

#bpy.ops.object.mode_set( mode = 'OBJECT' )
#obj.modifiers.new("subd", type='SUBSURF')
#obj.modifiers['subd'].levels = 1
bpy.ops.object.modifier_apply(modifier="subd")
obj.modifiers.new("skin", type='SKIN')
obj.modifiers.new("subd", type='SUBSURF')
obj.modifiers['subd'].levels = 1
grosores = []
grosor = 0.5
for i,v in enumerate(obj.data.skin_vertices[0].data):
    vActual = verts[i]
    vSiguiente = verts[i+1]
    dist = measure(vActual,vSiguiente)
    if i in raices:
        grosores.append(grosor)
    if dist > 1:
        grosor = grosores.pop()

    v.radius = grosor, grosor
    grosor = grosor - 0.5/len(verts)
