# Reconhcimento de placas de carros

## Protocolo de aquição (captura das fotos)

- As fotos foram tiradas com um celular Xiaomi Poco M3, com resolução de 12MP, com o aplicativo Open Camera, com a resolução máxima de 4000x3000 pixels, a cada foto eram efetuado 3 capturas com diferentes brilhos, para que fosse possível obter uma imagem com boa qualidade sem flash.

## Pré-processamento

- As imagens foram redimensionadas para 800x600 pixels, para que o processamento fosse mais rápido, e para que o modelo pudesse ser utilizado em tempo real.

- As imagens foram convertidas para escala de cinza, para que a cor não fosse um fator de interferência no reconhecimento.

- Foi utilizado do filtro de Canny para detectar as bordas da imagem, e assim facilitar a detecção dos caracteres.

- Posteriormente foi utilizado o tesseract para detectar os caracteres.