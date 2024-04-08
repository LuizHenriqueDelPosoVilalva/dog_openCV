import requests
from bs4 import BeautifulSoup

def contentHTML(site):
    url = site

    resposta = requests.get(url)

    if resposta.status_code == 200:

        # Criar objeto BeautifulSoup com o conteúdo da página
        soup = BeautifulSoup(resposta.content, "html.parser")

        # Encontrar todas as tags img
        imagens = soup.find_all("img")

        dados = {"imagens": []}

        # Extrair informações de cada imagem
        if imagens:
            for imagem in imagens:

                # Obter URL da imagem
                url_imagem = imagem["src"]

                # Obter legenda da imagem
                legenda = imagem["alt"]

                # Imprimir informações
                dados["imagens"].append({"url": url_imagem, "legenda": legenda})
        else:
            'Não é uma imagem'

        card_section = soup.find("div", class_="card-section-inner")
    
        pet_name = card_section.find("span", class_="u-displayBlock u-vr4x u-vr2x@minMd").text.strip()
        
        # Extrair raça e localização
        pet_breeds = card_section.find("span", class_="txt m-txt_bold txt_hasLink m-txt_lg@minMd").text.strip()
        pet_location = card_section.find("span", class_="txt m-txt_bold m-txt_lg@minMd").text.strip()

        # Imprimir informações
        dados["nome"] = pet_name
        dados["localização"] = pet_location
        dados["raça"] = pet_breeds

        return dados


    else:
        print("Erro ao acessar o site:", resposta.status_code)