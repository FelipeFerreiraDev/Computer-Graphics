import cv2
from PIL import Image

import numpy as np

# Import tesseract
import pytesseract

# Carrega a imagem
black = cv2.imread('Images/black car/IMG_20230701_115532_1.jpg')
red = cv2.imread('Images/red car/IMG_20230701_115717_0.jpg')
ana = cv2.imread('Images/ana car/WhatsApp Image 2023-07-04 at 08.32.31.jpeg')

def exibeImage(title, image):
    cv2.imshow(title, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def filtroGray(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Deixa imagem totalmente escura
def filtroThreshold(image, min, max):
    return cv2.threshold(image, min, max, cv2.THRESH_BINARY)

def filtroCanny(image, min, max):
    return cv2.Canny(image, min, max)

def redimensionaImage(image, width, height):
    return cv2.resize(image, (width, height))

def saveImage(image, name):
    cv2.imwrite('./tmp/'+name, image)

# Filtro de mediana
def filtroMediana(image, size):
    return cv2.medianBlur(image, size)

# Filtro de média
def filtroMedia(image, size):
    return cv2.blur(image, size)

# Filtro de Gauss
def filtroGauss(image, size):
    return cv2.GaussianBlur(image, size, 0)

# Filtro de Bilateral
def filtroBilateral(image, size):
    return cv2.bilateralFilter(image, size, 75, 75)

# Inverte branco e preto
def filtroInvert(image):
    return cv2.bitwise_not(image)

# Filtro de dilatação
def filtroDilatacao(image, size):
    return cv2.dilate(image, size, iterations=1)

# Filtro de erosão
def filtroErosao(image, size):
    return cv2.erode(image, size, iterations=1)

# Redimenciona a imagem
imagem_original = redimensionaImage(black, 800, 600)

# Converte para escala de cinza
imagem_gray = filtroGray(imagem_original)
exibeImage('Gray', imagem_gray)

# Aplica filtro de otsu
_, threshold = cv2.threshold(imagem_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
exibeImage('OTSU', threshold)

# Encontrando os contornos na imagem binarizada
contornos, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
exibeImage('Imagem findcontours', threshold)

# Iterando pelos contornos para encontrar os contornos com quatro lados
for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)

    if len(approx) == 4:  # Supõe que o conteúdo tem quatro lados
        cv2.drawContours(imagem_gray, [approx], 0, (0, 255, 0), 2)

exibeImage('Imagem black', imagem_gray)

# Iterando pelos contornos para encontrar o maior contorno com quatro lados
maior_contorno = None
maior_area = 0
for contorno in contornos:
    perimetro = cv2.arcLength(contorno, True)
    approx = cv2.approxPolyDP(contorno, 0.04 * perimetro, True)
    
    if len(approx) == 4:  # Supõe que o conteúdo tem quatro lados
        area = cv2.contourArea(contorno)

        if area > 100:

            # Criando uma máscara em branco do mesmo tamanho da imagem original
            mascara = np.zeros_like(imagem_gray)

            # Criando uma máscara em branco do mesmo tamanho da imagem original
            mascara_branca = np.ones_like(imagem_original) * 255

            # Desenhando o contorno do maior contorno na máscara branca
            cv2.drawContours(mascara_branca, [approx], 0, (0, 0, 0), -1)

            # Inverte a máscara para que a região fora do contorno fique branca
            mascara_invertida = cv2.bitwise_not(mascara_branca)

            # Aplicando a máscara invertida na imagem original
            imagem_cortada = cv2.bitwise_and(imagem_original, mascara_invertida)

            # Aplica o filtro de cinza
            imagem_cortada = filtroGray(imagem_cortada)
            exibeImage('Imagem gray', imagem_cortada)

            # Aplica filtro de otsu
            _, threshold = cv2.threshold(imagem_cortada, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
            exibeImage('OTSU', threshold)

            # Aplica o filtro de mediana
            imagem_cortada = filtroMediana(imagem_cortada, 3)
            exibeImage('Imagem mediana', imagem_cortada)

            text= pytesseract.image_to_string(imagem_cortada, lang='eng')
            if text != "" and len(text) > 1:
                print("detected " + text)
                sys.exit()

            text= pytesseract.image_to_string(imagem_cortada, config='--psm 11')
            if text != "" and len(text) > 1:
                print("detected " + text)
                sys.exit()