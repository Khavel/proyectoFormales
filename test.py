
import math
import bpy

orientacion = [0,1,0]
pos = [0,0,0]
brackets = []



def aplicarProducciones(palabra):

    nuevaPalabra = ""
    for simbolo in palabra:
        nuevaPalabra = nuevaPalabra + aplicarRegla(simbolo)

    return nuevaPalabra

def aplicarRegla(simbolo):
    if simbolo == "f":
        return "ff[-f]f[+f][f+]"
    elif simbolo == "b":
        return "b-"
    else:
        return simbolo



def makePoly(cadena):

    global orientacion
    global pos
    global verts
    global brackets
    vertCont = 0
    for c in cadena:

        if c == 'f':
            v = [pos[0] + orientacion[0],pos[1] + orientacion[1],0]
            pos = v
            verts.append(v)
            edges.append((vertCont,vertCont-1))
            vertCont = vertCont + 1
        elif c == '[':
            brackets.append((pos,orientacion))
        elif c == ']':
            pos_brackets,head_brackets = brackets.pop()
            pos = pos_brackets
            orientacion = head_brackets
        elif c == '+':
            dirX = orientacion[0]
            dirY = orientacion[1]
            if dirX == 0 and dirY == 1:
                orientacion = [1,1,0]

            elif dirX == 1 and dirY == 1:
                orientacion = [1,0,0]

            elif dirX == 1 and dirY == 0:
                orientacion = [1,-1,0]

            elif dirX == 1 and dirY == -1:
                orientacion = [0,-1,0]

            elif dirX == 0 and dirY == -1:
                orientacion = [-1,-1,0]

            elif dirX == -1 and dirY == -1:
                orientacion = [-1,0,0]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,1,0]

            elif dirX == -1 and dirY == 1:
                orientacion = [0,1,0]


        elif c == '-':
            dirX = orientacion[0]
            dirY = orientacion[1]


            if dirX == 0 and dirY == 1:
                orientacion = [-1,1,0]

            elif dirX == 1 and dirY == 1:
                orientacion = [0,1,0]

            elif dirX == 1 and dirY == 0:
                orientacion = [1,1,0]

            elif dirX == 1 and dirY == -1:
                orientacion = [1,0,0]

            elif dirX == 0 and dirY == -1:
                orientacion = [1,-1,0]

            elif dirX == -1 and dirY == -1:
                orientacion = [0,-1,0]

            elif dirX == -1 and dirY == 0:
                orientacion = [-1,-1,0]

            elif dirX == -1 and dirY == 1:
                orientacion = [-1,0,0]

            elif c == '*':
                dirX = orientacion[0]
                dirY = orientacion[1]
                dirZ = orientacion[2]

                if dirX == 0 and dirY == 1:
                    orientacion = [-1,1,0]

                elif dirX == 1 and dirY == 1:
                    orientacion = [0,1,0]

                elif dirX == 1 and dirY == 0:
                    orientacion = [1,1,0]

                elif dirX == 1 and dirY == -1:
                    orientacion = [1,0,0]

                elif dirX == 0 and dirY == -1:
                    orientacion = [1,-1,0]

                elif dirX == -1 and dirY == -1:
                    orientacion = [0,-1,0]

                elif dirX == -1 and dirY == 0:
                    orientacion = [-1,-1,0]

                elif dirX == -1 and dirY == 1:
                    orientacion = [-1,0,0]




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
edges.append((0,len(edges)-1))
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

bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})
bpy.ops.mesh.extrude_region_move(TRANSFORM_OT_translate={"value":(0, 0, 3)})


bpy.ops.object.mode_set( mode = 'OBJECT' )
