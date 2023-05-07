from PIL import Image

# Inverte a imagem horizontalmente
def inverte_horizontal(imagem):
    largura, altura = imagem.size
    nova_imagem = imagem.copy()
    for y in range(altura):
        for x in range(largura // 2):
            esquerda = nova_imagem.getpixel((x, y))
            direita = nova_imagem.getpixel((largura - 1 - x, y))
            nova_imagem.putpixel((x, y), direita)
            nova_imagem.putpixel((largura - 1 - x, y), esquerda)
    return nova_imagem

# Inverte a imagem verticalmente
def inverte_vertical(imagem):
    largura, altura = imagem.size
    nova_imagem = imagem.copy()
    for y in range(altura // 2):
        for x in range(largura):
            topo = nova_imagem.getpixel((x, y))
            base = nova_imagem.getpixel((x, altura - 1 - y))
            nova_imagem.putpixel((x, y), base)
            nova_imagem.putpixel((x, altura - 1 - y), topo)
    return nova_imagem

imagem = Image.open("Images/imagem.jpg")
imagem_invertida_horizontal = inverte_horizontal(imagem)
imagem_invertida_vertical = inverte_vertical(imagem)
imagem_invertida_horizontal.show()
imagem_invertida_vertical.show()