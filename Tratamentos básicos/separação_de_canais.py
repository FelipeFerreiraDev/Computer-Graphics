from PIL import Image

# Leitura da imagem
img = Image.open('Images/imagem.jpg')

# Separação dos canais RGB
r, g, b = img.split()

# Exibição de cada canal separadamente
r.show()
g.show()
b.show()