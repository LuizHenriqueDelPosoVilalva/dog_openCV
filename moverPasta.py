import os
import random

def mover_pastas(pasta_raiz, pasta_destino_25, pasta_destino_75):
  
  # Lista todas as pastas na pasta raiz
  pastas = os.listdir(pasta_raiz)

  # Embaralha a lista de pastas
  random.shuffle(pastas)

  # Número de pastas a serem movidas para cada pasta de destino
  numero_pastas_25 = 12
  numero_pastas_75 = 38

  # Move as pastas para as pastas de destino
  for i in range(numero_pastas_25):
    pasta = pastas.pop()
    os.rename(os.path.join(pasta_raiz, pasta), os.path.join(pasta_destino_25, pasta))

  for i in range(numero_pastas_75):
    pasta = pastas.pop()
    os.rename(os.path.join(pasta_raiz, pasta), os.path.join(pasta_destino_75, pasta))