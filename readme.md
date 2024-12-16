Projeto para redução de dimensionalidade em imagens.


Seguindo o exemplo do algoritmo de binarização apresentado em nossa última aula, realize a implementação em Python para transformar uma imagem colorida para níveis de cinza (0 a 255) e para binarizada (0 e 255), preto e branco.

Passo 1: Importar Bibliotecas Necessárias
Use as bibliotecas Pillow para manipular imagens e matplotlib para exibir os resultados.

python
Copiar código
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
Passo 2: Carregar uma Imagem Colorida
Carregue a imagem colorida que será transformada.

python
Copiar código
# Carregar a imagem (substitua 'sua_imagem.jpg' pelo caminho da sua imagem)
imagem_colorida = Image.open('sua_imagem.jpg')

# Mostrar a imagem original
plt.imshow(imagem_colorida)
plt.title("Imagem Colorida")
plt.axis("off")
plt.show()
Passo 3: Converter para Tons de Cinza
Transforme a imagem em tons de cinza, com valores variando entre 0 e 255.

python
Copiar código
# Converter para tons de cinza
imagem_cinza = imagem_colorida.convert('L')

# Mostrar a imagem em tons de cinza
plt.imshow(imagem_cinza, cmap='gray')
plt.title("Imagem em Tons de Cinza")
plt.axis("off")
plt.show()
Passo 4: Binarizar a Imagem
Converta os níveis de cinza para uma imagem binária (preto e branco) com base em um limiar.

python
Copiar código
# Converter a imagem para um array numpy
imagem_array = np.array(imagem_cinza)

# Definir o limiar para binarização
limiar = 128
imagem_binarizada = (imagem_array > limiar) * 255  # Valores acima do limiar ficam brancos (255)

# Mostrar a imagem binarizada
plt.imshow(imagem_binarizada, cmap='gray')
plt.title("Imagem Binarizada (Preto e Branco)")
plt.axis("off")
plt.show()
Passo 5: Salvar os Resultados (Opcional)
Salve as imagens geradas, caso necessário.

python
Copiar código
# Salvar as imagens em cinza e binarizada
imagem_cinza.save('imagem_cinza.jpg')
Image.fromarray(imagem_binarizada.astype(np.uint8)).save('imagem_binarizada.jpg')
Resultado Final
A imagem colorida será exibida em três etapas:
Original.
Em tons de cinza.
Binarizada em preto e branco.