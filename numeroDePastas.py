import os

def contar_pastas(pasta_raiz):

  numero_pastas = 0

  # Lista todos os arquivos e pastas na pasta raiz
  arquivos_e_pastas = os.listdir(pasta_raiz)

  # Itera sobre cada arquivo e pasta
  for arquivo_ou_pasta in arquivos_e_pastas:
    # Verifica se é uma pasta
    if os.path.isdir(os.path.join(pasta_raiz, arquivo_ou_pasta)):
      numero_pastas += 1

  return numero_pastas