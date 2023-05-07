import numpy as np
from PIL import Image

# Carrega a imagem em tons de cinza
img = Image.open('Images/imagem.jpg').convert('L')
img_array = np.array(img)

# Define o valor de limiarização (threshold) manualmente
threshold = 128

# Converte a imagem em preto e branco com limiarização manual
bw_array = np.where(img_array > threshold, 255, 0)

# Exibe a imagem em preto e branco
bw_img = Image.fromarray(bw_array.astype(np.uint8))
bw_img.show()
