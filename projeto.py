from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem colorida
imagem_colorida = Image.open('sua_imagem.jpg')

# Mostrar a imagem colorida
plt.imshow(imagem_colorida)
plt.title("Imagem Colorida")
plt.axis("off")
plt.show()

# Converter para tons de cinza
imagem_cinza = imagem_colorida.convert('L')
plt.imshow(imagem_cinza, cmap='gray')
plt.title("Imagem em Tons de Cinza")
plt.axis("off")
plt.show()

# Binarizar a imagem
imagem_array = np.array(imagem_cinza)
limiar = 128
imagem_binarizada = (imagem_array > limiar) * 255

# Mostrar a imagem binarizada
plt.imshow(imagem_binarizada, cmap='gray')
plt.title("Imagem Binarizada (Preto e Branco)")
plt.axis("off")
plt.show()

# Salvar os resultados
imagem_cinza.save('imagem_cinza.jpg')
Image.fromarray(imagem_binarizada.astype(np.uint8)).save('imagem_binarizada.jpg')
