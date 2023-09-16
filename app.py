import os
from PIL import Image, ImageDraw, ImageFont


caminho_img = "imagens-recortardas/D053_recorte.png"



# TESTE DE ESCRITA EM IMAGENS
path_font = "arial.ttf"
font = ImageFont.truetype(path_font, 48)
# im = Image.new("RGB", (200, 200), "white")
im = Image.open(caminho_img)


w,h = im.size
posicao_texto = (10,500)

d = ImageDraw.Draw(im)
# d.line(((0, 100), (200, 100)), "gray")
# d.line(((100, 0), (100, 200)), "gray")
d.text(posicao_texto, "Quick", fill="black", font=font)
im.save("teste1.jpg")