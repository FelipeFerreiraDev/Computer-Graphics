from PIL import Image

# Abre a imagem
imagem = Image.open("Images/imagem.jpg")

# Utiliza o rotate com a angulação desejada
imagem_rotate = imagem.rotate(90, expand=True)

# Cria uma nova imagem do tamanho necessário para conter a imagem girada
nova_imagem = Image.new('RGBA', imagem_rotate.size, (255, 255, 255, 0))

# Cola a imagem girada no centro da nova imagem
posicao = ((nova_imagem.size[0] - imagem_rotate.size[0]) // 2, (nova_imagem.size[1] - imagem_rotate.size[1]) // 2)
nova_imagem.paste(imagem_rotate, posicao)

# Exibe a imagem
imagem_rotate.show()