from PIL import Image

# Abrindo a imagem em RGB
imagem_rgb = Image.open("Images/imagem.jpg")

# Obtendo as dimensões da imagem
width, height = imagem_rgb.size

# Criando uma nova imagem em tons de cinzaSalva
imagem_cinza = Image.new("L", (width, height))

# Percorrendo cada pixel da imagem RGB e convertendo em um pixel em tons de cinza
for x in range(width):
    for y in range(height):
        # Obtendo os valores RGB do pixel atual
        r, g, b = imagem_rgb.getpixel((x, y))

        # Calculando a média ponderada dos valores RGB para obter o valor em tons de cinza
        valor_cinza = int(0.299 * r + 0.587 * g + 0.114 * b)

        # Definindo o novo valor em tons de cinza para o pixel atual na nova imagem
        imagem_cinza.putpixel((x, y), valor_cinza)

# Exibindo a nova imagem em tons de cinza
imagem_cinza.show()
