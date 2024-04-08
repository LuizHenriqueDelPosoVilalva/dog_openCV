from contentHtmlPetFinder import contentHTML
from dowloadImgPetFinder import criar_pasta_e_baixar_img
from numeroDePastas import contar_pastas
from moverPasta import mover_pastas
    
numero_pastas = contar_pastas("img_dogs")
quantidade_25 = contar_pastas("dogs_25")
quantidade_75 = contar_pastas("dogs_75")

# Imprime o número de pastas
print(f"Número de pastas em img_dog: {numero_pastas}")
print(f"Número de pastas em dogs_25: {quantidade_25}")
print(f"Número de pastas em dogs_75: {quantidade_75}")

#url = "https://www.petfinder.com/dog/lola-53825792/pr/san-juan/save-a-sato-foundation-pr26/"
#pasta_raiz = "dogs_75"

#dados = contentHTML(url)

#criar_pasta_e_baixar_img(dados, pasta_raiz)

#contar_pastas(pasta_raiz)
    
# Executa a função para mover as pastas
#mover_pastas(pasta_raiz, "dogs_25", "dogs_75")