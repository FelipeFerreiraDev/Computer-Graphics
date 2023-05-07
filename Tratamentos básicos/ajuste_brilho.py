from PIL import Image

# Abre a imagem
img = Image.open('Images/imagem.jpg')

# Define o fator de brilho desejado
fator_brilho = 1.5

# Obtém a largura e altura da imagem
width, height = img.size

# Percorre cada pixel da imagem e aplica o fator de brilho
for x in range(width):
    for y in range(height):
        r, g, b = img.getpixel((x, y))
        r = int(r * fator_brilho)
        g = int(g * fator_brilho)
        b = int(b * fator_brilho)
        img.putpixel((x, y), (r, g, b))

# Exibe a imagem com o brilho ajustado
img.show()
