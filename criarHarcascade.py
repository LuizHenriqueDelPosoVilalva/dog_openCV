import cv2
import numpy as np
import os

# Função para carregar as imagens de um diretório
def carregar_imagens(diretorio):
    imagens = []
    for diretorio_raiz, subdiretorios, arquivos in os.walk(diretorio):
        for nome_arquivo in arquivos:
            caminho = os.path.join(diretorio_raiz, nome_arquivo)
            imagem = cv2.imread(caminho)
            if imagem is not None:
                imagens.append(imagem)
    
    return imagens

# Função para extrair amostras positivas e criar o arquivo positives.dat
def criar_positives_dat(imagens_positivas):
    with open('positives.dat', 'w') as f:
        for imagem in imagens_positivas:
            gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
            altura, largura = imagem.shape[:2]
            f.write(f'{largura} {altura} 1\n')  # Grava largura, altura e o rótulo
            # Salvar a imagem em escala de cinza
            for linha in gray:
                np.savetxt(f, linha, fmt='%i')

# Função para criar o arquivo negatives.txt
def criar_negatives_txt(diretorio_negativos):
    with open('negatives.txt', 'w') as f:
        for nome_arquivo in os.listdir(diretorio_negativos):
            caminho_completo = os.path.join(diretorio_negativos, nome_arquivo)
            f.write(f'{caminho_completo}\n')

# Diretório contendo as imagens positivas
diretorio_positivos = 'dogs_75'
# Diretório contendo as imagens negativas
diretorio_negativos = 'img_negativa'

# Carregar imagens positivas
imagens_positivas = carregar_imagens(diretorio_positivos)

# Criar o arquivo positives.dat
criar_positives_dat(imagens_positivas)

# Criar o arquivo negatives.txt
criar_negatives_txt(diretorio_negativos)

# Comando para treinar o classificador haar cascade
# Comando para treinar o classificador haar cascade
os.system(f'opencv_traincascade -data cascades -vec positives.dat -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 1000 -numNeg 600 -w 24 -h 24 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024')


# Após o treinamento, você obterá o arquivo XML do classificador no diretório 'cascades'
