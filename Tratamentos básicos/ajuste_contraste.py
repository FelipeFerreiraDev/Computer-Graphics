from PIL import Image
import numpy as np

# Carregando a imagem
im = Image.open('Images/imagem.jpg')

# Convertendo a imagem em um array numpy
img = np.asarray(im)

# Calculando o mínimo e o máximo dos valores de pixel
min_val = np.min(img)
max_val = np.max(img)

# Ajustando o contraste
img_contrast = ((img - min_val) * (255.0 / (max_val - min_val))).astype(np.uint8)

# Exibendo a imagem
Image.fromarray(img_contrast).show()
