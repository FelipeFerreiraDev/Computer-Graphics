from PIL import Image

# Abre a imagem
img = Image.open("Images/imagem.jpg")

# Converte a imagem para escala de cinza
gray_img = img.convert("L")

# Cria uma nova imagem em escala de cinza
mean_img = Image.new('L', img.size)

# Itera por cada pixel na imagem original e calcula a conversão em escala de cinza
for x in range(2,gray_img.width-1):
    for y in range(2,gray_img.height-1):
        # Obtem o valor do pixel em RGB
        gray = gray_img.getpixel((x, y))

        # calcula média da janela 3x3
        mean_value = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                mean_value += gray_img.getpixel((x + i, y + j))
        mean_value //= 9
        

        # Define o novo pixel na imagem em escala de cinza
        mean_img.putpixel((x, y), mean_value)

# Exibe a imagem em escala de cinza
mean_img.show()
