import os
import requests

def criar_pasta_e_baixar_img(dados, pasta_raiz):

    # Criar pasta para o animal
    pasta_animal = os.path.join(pasta_raiz, dados["nome"])
    os.makedirs(pasta_animal, exist_ok=True)

    imagens_selecionadas = dados["imagens"][:5]

    # Baixar imagens
    for imagem in imagens_selecionadas:
        if imagem["legenda"]:
            url_imagem = imagem["url"]
            nome_arquivo = imagem["legenda"]
            
            arquivo = f"{nome_arquivo}.jpeg"

            with requests.get(url_imagem, stream=True) as r:
                with open(os.path.join(pasta_animal, arquivo), "wb") as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        f.write(chunk)