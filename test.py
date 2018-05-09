
import math
import bpy

orientacion = [1,1,0]
pos = [0,0,0]
brackets = []



def aplicarProducciones(palabra):

    nuevaPalabra = ""
    for simbolo in palabra:
        nuevaPalabra = nuevaPalabra + aplicarRegla(simbolo)

    return nuevaPalabra

def aplicarRegla(simbolo):
    if simbolo == "f":
        return "*f+b[-f/]b[+f*][b+]"
    elif simbolo == "b":
        return "b-fbb[++f]fb"
    else:
        return simbolo



def makePoly(cadena):

    global orientacion
    global pos
    global verts
    global brackets
    vertCont = 0
    trasBracket = False
    for c in cadena:

        if c == 'f':
            v = [pos[0] + orientacion[0],pos[1] + orientacion[1],pos[2] + orientacion[2]]
            pos = v
            if not v in verts:
                verts.append(v)
                vertCont = vertCont + 1
                if not trasBracket:
                    edges.append((vertCont,vertCont-1))
                else:
                    trasBracket = False

        if c == 'b':
            v = [pos[0] - orientacion[0],pos[1] - orientacion[1],pos[2] - orientacion[2]]
            pos = v
            if not v in verts:
                verts.append(v)
                vertCont = vertCont + 1
                if not trasBracket:
                    edges.append((vertCont,vertCont-1))
                else:
                    trasBracket = False


        #Guarda la posicion
        elif c == '[':
            brackets.append((pos,orientacion))

        #Retorna a la ultima posicion guardada
        elif c == ']':
            pos_brackets,head_brackets = brackets.pop()
            pos = pos_brackets
            orientacion = head_brackets
            trasBracket = True

        elif c == '+':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]
            if dirX == 0 and dirY == 1:
                orientacion = [1,1,dirZ]

            elif dirX == 1 and dirY == 1:
                orientacion = [1,0,dirZ]

            elif dirX == 1 and dirY == 0:
                orientacion = [1,-1,dirZ]

            elif dirX == 1 and dirY == -1:
                orientacion = [0,-1,dirZ]

            elif dirX == 0 and dirY == -1:
                orientacion = [-1,-1,dirZ]

            elif dirX == -1 and dirY == -1:
                orientacion = [-1,0,dirZ]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,1,dirZ]

            elif dirX == -1 and dirY == 1:
                orientacion = [0,1,dirZ]


        elif c == '-':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirX == 0 and dirY == 1:
                orientacion = [-1,1,dirZ]

            elif dirX == 1 and dirY == 1:
                orientacion = [0,1,dirZ]

            elif dirX == 1 and dirY == 0:
                orientacion = [1,1,dirZ]

            elif dirX == 1 and dirY == -1:
                orientacion = [1,0,dirZ]

            elif dirX == 0 and dirY == -1:
                orientacion = [1,-1,dirZ]

            elif dirX == -1 and dirY == -1:
                orientacion = [0,-1,dirZ]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,-1,dirZ]

            elif dirX == -1 and dirY == 1:
                orientacion = [-1,0,dirZ]

            #Hacia arriba
        elif c == '*':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirZ == 0:
                orientacion = [dirX,dirY,1]

            elif dirZ == 1:
                v = [pos[0],pos[1],pos[2] + 1]
                pos = v
                if not v in verts:
                    verts.append(v)
                    vertCont = vertCont + 1
                    edges.append((vertCont,vertCont-1))

            elif dirZ == -1:
                orientacion = [dirX,dirY,0]
            #Hacia abajo
        elif c == '/':
            dirX = orientacion[0]
            dirY = orientacion[1]
            dirZ = orientacion[2]

            if dirZ == 0:
                orientacion = [dirX,dirY,-1]

            elif dirZ == 1:
                orientacion = [dirX,dirY,0]

            elif dirZ == -1:
                v = [pos[0],pos[1],pos[2] - 1]
                pos = v
                if not v in verts:
                    verts.append(v)
                    vertCont = vertCont + 1
                    edges.append((vertCont,vertCont-1))





verts=[]
edges = []
faces = []


vueltas = 5
palabra = "f"
for i in range(vueltas):
    palabra = palabra + aplicarProducciones(palabra)

#print palabra
makePoly(palabra)


mesh = bpy.data.meshes.new("test");
#edges.append((0,len(edges)-1))
mesh.from_pydata(verts, edges, faces)
mesh.validate(True)
mesh.show_normal_face = True

obj = bpy.data.objects.new("test", mesh)
scn = bpy.context.scene
scn.objects.link(obj)

bpy.context.scene.objects.active = obj

bpy.ops.object.mode_set(mode='EDIT', toggle=True)
bpy.ops.mesh.select_mode( type  = 'VERT')
bpy.ops.mesh.select_all( action = 'SELECT')

#bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})
#bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})


bpy.ops.object.mode_set( mode = 'OBJECT' )
