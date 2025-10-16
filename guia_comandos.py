# Guia Prático de Comandos OpenCV e OS
# ---------------------------------

"""
Este guia contém os principais comandos usados no OpenCV (cv2) e módulo OS,
com exemplos práticos de uso.
"""

# ---- Comandos do módulo OS para manipulação de arquivos ----

'''
1. os.path.join()
   - O que faz: Cria caminhos de arquivo de forma segura para qualquer sistema operacional
   - Uso: Para construir caminhos para imagens/vídeos
'''
import os
# Exemplo:
caminho_imagem = os.path.join("data", "foto.jpg")  # Resulta em "data/foto.jpg" no Linux/Mac


'''
2. os.listdir()
   - O que faz: Lista todos os arquivos em um diretório
   - Uso: Para processar múltiplas imagens em uma pasta
'''
# Exemplo:
arquivos_imagens = [f for f in os.listdir("data") if f.endswith(('.jpg', '.png'))]


# ---- Comandos OpenCV para Leitura e Exibição ----

'''
1. cv2.imread()
   - O que faz: Carrega uma imagem do arquivo
   - Uso: Quando precisar abrir qualquer imagem
'''
import cv2
# Exemplo:
img = cv2.imread("data/foto.jpg")  # Carrega em BGR
img = cv2.imread("data/foto.jpg", cv2.IMREAD_GRAYSCALE)  # Carrega em tons de cinza


'''
2. cv2.imshow() + cv2.waitKey()
   - O que faz: Exibe uma imagem em uma janela
   - Uso: Para visualizar imagens durante o desenvolvimento
'''
# Exemplo:
cv2.imshow("Janela", img)
cv2.waitKey(0)  # Espera pressionar qualquer tecla
cv2.destroyAllWindows()


'''
3. cv2.VideoCapture()
   - O que faz: Abre um vídeo ou webcam
   - Uso: Para processar vídeos ou captura em tempo real
'''
# Exemplo - Arquivo de vídeo:
video = cv2.VideoCapture("video.mp4")

# Exemplo - Webcam:
webcam = cv2.VideoCapture(0)  # 0 é a webcam padrão


'''
4. cv2.resize()
   - O que faz: Redimensiona uma imagem
   - Uso: Quando precisar mudar o tamanho de uma imagem
'''
# Exemplo:
img_redimensionada = cv2.resize(img, (300, 200))  # Largura=300, Altura=200


# ---- Grupos de Funções OpenCV para Processamento ----

# ==== 1. GRUPO: Conversão de Cores ====
'''
cv2.cvtColor()
- O que faz: Converte entre espaços de cor
- Uso comum: BGR ↔ RGB ↔ HSV ↔ Grayscale

Espaços de cor importantes:
- cv2.COLOR_BGR2GRAY: Para processamento em tons de cinza
- cv2.COLOR_BGR2HSV: Para segmentação por cor (H=matiz, S=saturação, V=valor)
- cv2.COLOR_BGR2RGB: Para exibição correta em matplotlib/notebooks
'''
# Exemplo:
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


# ==== 2. GRUPO: Filtros de Suavização ====
'''
A. cv2.GaussianBlur(img, (ksize), sigma)
   - ksize: Tamanho do kernel (SEMPRE ÍMPAR: 3x3, 5x5, 7x7)
   - sigma: Desvio padrão (0 = automático)
   - Uso: Redução de ruído preservando bordas
'''
img_gauss = cv2.GaussianBlur(img, (5,5), 0)

'''
B. cv2.medianBlur(img, ksize)
   - ksize: Tamanho do kernel (SEMPRE ÍMPAR)
   - Uso: Melhor para ruído tipo "sal e pimenta"
'''
img_median = cv2.medianBlur(img, 5)

'''
C. cv2.blur(img, (ksize))
   - Média simples
   - Uso: Suavização básica, mais rápido que Gaussian
'''
img_blur = cv2.blur(img, (5,5))


# ==== 3. GRUPO: Detecção de Bordas ====
'''
A. cv2.Canny(img, threshold1, threshold2, apertureSize=3)
   - threshold1: Limiar mínimo (sugestão: 100)
   - threshold2: Limiar máximo (sugestão: 200)
   - apertureSize: Tamanho Sobel (3=suave, 5=mais detalhado)
   
   Dica: Razão 1:2 ou 1:3 entre thresholds geralmente funciona bem
'''
bordas = cv2.Canny(img_gray, 100, 200)

'''
B. cv2.Sobel(img, ddepth, dx, dy, ksize)
   - ddepth: Profundidade (-1 = mesma da imagem)
   - dx, dy: Ordem da derivada (1,0=vertical, 0,1=horizontal)
   - ksize: Tamanho do kernel (1,3,5,7)
'''
sobelx = cv2.Sobel(img_gray, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(img_gray, cv2.CV_64F, 0, 1, ksize=5)


# ==== 4. GRUPO: Thresholding (Binarização) ====
'''
A. cv2.threshold(img, thresh, maxval, type)
   - thresh: Valor do limiar (ex: 127)
   - maxval: Valor máximo (ex: 255)
   - type: Método de threshold:
     * cv2.THRESH_BINARY: Acima do limiar = maxval, abaixo = 0
     * cv2.THRESH_BINARY_INV: Inverso do BINARY
     * cv2.THRESH_TRUNC: Acima do limiar = limiar
     * cv2.THRESH_OTSU: Encontra limiar automaticamente
'''
# Threshold simples
_, bin_simples = cv2.threshold(img_gray, 127, 255, cv2.THRESH_BINARY)

# Threshold Otsu (automático)
_, bin_otsu = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

'''
B. cv2.adaptiveThreshold(img, maxval, method, type, blockSize, C)
   - method: cv2.ADAPTIVE_THRESH_MEAN_C ou GAUSSIAN_C
   - blockSize: Tamanho da vizinhança (ÍMPAR)
   - C: Constante subtraída da média
   - Uso: Melhor para imagens com iluminação variável
'''
adapt_thresh = cv2.adaptiveThreshold(img_gray, 255, 
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY, 11, 2)


# ==== 5. GRUPO: Operações Morfológicas ====
'''
Funções: cv2.erode(), cv2.dilate(), cv2.morphologyEx()
Kernel: cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

Operações principais:
- MORPH_ERODE: Diminui áreas brancas
- MORPH_DILATE: Aumenta áreas brancas
- MORPH_OPEN: Erosão seguida de dilatação (remove ruído)
- MORPH_CLOSE: Dilatação seguida de erosão (fecha buracos)
'''
# Criando elemento estruturante
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))

# Exemplos
img_erode = cv2.erode(img, kernel, iterations=1)
img_dilate = cv2.dilate(img, kernel, iterations=1)
img_open = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img_close = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)


# ==== 6. GRUPO: Contornos ====
'''
Workflow típico:
1. Converter para grayscale
2. Aplicar threshold/Canny
3. Encontrar contornos
4. Analisar/desenhar contornos

A. cv2.findContours(img, mode, method)
   - img: Imagem binária (preto e branco)
   - mode: 
     * cv2.RETR_EXTERNAL: Apenas contornos externos
     * cv2.RETR_TREE: Todos os contornos + hierarquia
   - method:
     * cv2.CHAIN_APPROX_SIMPLE: Apenas pontos extremos
     * cv2.CHAIN_APPROX_NONE: Todos os pontos
'''
# Exemplo básico
contours, hierarchy = cv2.findContours(img, 
                                     cv2.RETR_EXTERNAL,
                                     cv2.CHAIN_APPROX_SIMPLE)

'''
B. cv2.drawContours(img, contours, contourIdx, color, thickness)
   - img: Imagem onde desenhar
   - contours: Lista de contornos
   - contourIdx: Índice do contorno (-1 = todos)
   - color: Cor do desenho (ex: (0,255,0) para verde)
   - thickness: Espessura da linha (-1 = preenchido)
'''
# Desenhar todos os contornos em verde
img_contours = img.copy()
cv2.drawContours(img_contours, contours, -1, (0,255,0), 2)

'''
C. Análise de Contornos
Funções úteis para cada contorno:
- cv2.contourArea(): Área do contorno
- cv2.arcLength(): Perímetro do contorno
- cv2.boundingRect(): Retângulo delimitador
- cv2.minAreaRect(): Retângulo rotacionado mínimo
- cv2.approxPolyDP(): Aproximação poligonal
'''
# Exemplo de análise
for cnt in contours:
    # Área
    area = cv2.contourArea(cnt)
    
    # Perímetro
    perimeter = cv2.arcLength(cnt, True)  # True = contorno fechado
    
    # Retângulo delimitador
    x, y, w, h = cv2.boundingRect(cnt)
    cv2.rectangle(img_contours, (x,y), (x+w,y+h), (255,0,0), 2)
    
    # Aproximação poligonal (simplifica forma)
    epsilon = 0.02 * perimeter  # 2% do perímetro
    approx = cv2.approxPolyDP(cnt, epsilon, True)
    
    # Detectar formas pelo número de vértices
    vertices = len(approx)
    if vertices == 3:
        shape = "Triangulo"
    elif vertices == 4:
        shape = "Retangulo/Quadrado"
    elif vertices > 8:
        shape = "Circulo"

'''
D. Filtragem de Contornos
Dicas para filtrar contornos por:
- Área: Remover ruídos pequenos ou objetos grandes demais
- Razão de aspecto: Identificar formas específicas
- Convexidade: Distinguir formas côncavas/convexas
'''
# Exemplo de filtragem por área
contornos_filtrados = [cnt for cnt in contours 
                      if cv2.contourArea(cnt) > 100]  # área mínima


# ---- Comandos OpenCV para Salvamento ----

'''
1. cv2.imwrite()
   - O que faz: Salva uma imagem em arquivo
   - Uso: Para salvar resultados do processamento
'''
# Exemplo:
cv2.imwrite("resultado.jpg", img)


'''
2. cv2.imencode()
   - O que faz: Codifica imagem para buffer de memória
   - Uso: Para enviar imagens pela rede ou exibir em notebooks
'''
# Exemplo:
_, buffer = cv2.imencode('.jpg', img)
bytes_imagem = buffer.tobytes()


# Dicas de Produtividade:
# 1. Sempre verifique se imagens/vídeos foram carregados corretamente:
if img is None:
    print("Erro ao carregar imagem")

# 2. Para vídeos, sempre libere os recursos:
video.release()
cv2.destroyAllWindows()

# 3. Para webcam, verifique se está disponível:
if not webcam.isOpened():
    print("Erro ao acessar webcam")

# 4. Use try-except para operações que podem falhar:
try:
    img = cv2.imread("imagem.jpg")
    # processamento...
except Exception as e:
    print(f"Erro: {e}")
finally:
    cv2.destroyAllWindows()