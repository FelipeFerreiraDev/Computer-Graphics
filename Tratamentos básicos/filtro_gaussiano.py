from PIL import Image, ImageFilter

# Abrir a imagem
imagem = Image.open("Images/imagem.jpg")

# Aplicar o filtro de desfoque gaussiano
imagem_desfocada = imagem.filter(ImageFilter.GaussianBlur(radius=2))

# Exiber a imagem desfocada
imagem_desfocada.show()