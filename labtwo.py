from gl import Render, color, linalgNormal
from obj import ObjFile, Texture
from shaders import *

# inicializar el render y cargar modelo
r = Render(800, 800)

## THERMAL VISION ##

# activar shader thermal vision
r.active_shader = thermalVision

# color de fondo azul para el primer shader
r.glClearColor(20 / 255, 20 / 255, 70 / 255)
r.glClear()

# renderizar shader
print("Dibujando modelo 1...")

r.glLoadObj('model.obj', (400, 400, 0), (300, 300, 300))
r.glFinish('thermal_vision.bmp')

print("Finalizado")

## TOON ##

# activar shader
r.active_shader = toonShader

# fondo negro
r.glClearColor(0, 0, 0)
r.glClear()

# finalizar shader
print("\nDibujando modelo 2...")

r.glLoadObj('model.obj', (400, 400, 0), (300, 300, 300))
r.glFinish('toon.bmp')
print("Finalizado")


## GOURAD ##

# cargar textura y hacer el set
texture = Texture('model.bmp')
r.glSetTexture(texture)

# activar shader
r.active_shader = gourad

# fondo negro
r.glClearColor(0, 0, 0)
r.glClear()

# finalizar shader
print("\nDibujando modelo 3...")

r.glLoadObj('model.obj', (400, 400, 0), (300, 300, 300))
r.glFinish('gourad.bmp')

print("Finalizado")
