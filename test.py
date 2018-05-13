
import bpy
import sys
sys.path.append("C:/Users/aot70/Desktop/proyectoFormales/")
import TortugaBlender
from TortugaBlender import *


vueltas = 3
palabra = "f"
tortuga = TortugaBlender()
for i in range(vueltas):
    palabra = palabra + tortuga.aplicarProducciones(palabra)

verts,edges,faces,vverts = tortuga.makePoly(palabra)

mesh = bpy.data.meshes.new("test");
mesh.from_pydata(verts, edges, faces)
mesh.validate(True)
mesh.show_normal_face = True

obj = bpy.data.objects.new("test", mesh)
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

for i,v in enumerate(obj.data.skin_vertices[0].data):
    if i in vverts:
        v.radius = 0.02, 0.02
