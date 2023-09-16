import os
from PIL import Image,ImageDraw,ImageFont
from joblib import Parallel, delayed
from os import path
from time import sleep




class GeradorCatalog:
    PATH_DESTINO_IMGS_RECORTADAS = "imagens-recortardas"
    def __init__(self,pasta_imagens=".") -> None:
        self.pasta_imagens= pasta_imagens
        
        
    def recortar_image(self,caminho_img,box):
        img = Image.open(caminho_img)
        nova_img = img.crop(box)
        novo_nome = self.gerar_novo_nome(caminho_img)["novo_nome"]
        destino = os.path.join(
            GeradorCatalog.PATH_DESTINO_IMGS_RECORTADAS
            , novo_nome)
        nova_img.save(destino)
      
      
    # Preciso implementar rsrs  
    # def escrever_img(img,texto,xy=(10,500)):
    #     font = ImageFont.truetype("arial.ttf")
    #     draw = ImageDraw.Draw(img)
    #     draw.text(xy,texto,fill="red",font=font)
        
        
        
    def gerar_novo_nome(self,arquivo,complemento="_recorte"):
        raiz,caminho = path.split(arquivo)
        nome,_ = path.splitext(caminho)
        # print(nome)-
        return {"novo_nome":f"{nome}{complemento}.png","nome_limpo":nome} 
        
        
    def imagens_validas(self,extensao=""):
        return list(
            map(
                lambda img:os.path.join(self.pasta_imagens,img) ,
                os.listdir(self.pasta_imagens)
                )
            )
    
    
box = (0, 0, 567, 567)

gerador_catalogo = GeradorCatalog("imagens-bases")
print(gerador_catalogo.imagens_validas())

for img in gerador_catalogo.imagens_validas():
    i = Image.open(img)
    resultado = Parallel(n_jobs=3)(lambda x: gerador_catalogo.recortar_image)(img,box)
    
    