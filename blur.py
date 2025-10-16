import cv2
import os

img_path = os.path.join("data", "edgy.jpg")
img = cv2.imread(img_path)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

img_blur = cv2.blur(img, (13,13))
img_gauss_blur = cv2.GaussianBlur(img, (13,13), 7)
img_median_blur = cv2.medianBlur(img, 13)
img_bilateral = cv2.bilateralFilter(img, 100, 100, 100)

if img is None:
    print("Erro ao carregar a imagem.")
else:
    # cv2.imshow("foto", img_blur)
    # cv2.imshow("foto2", img_gauss_blur)
    # cv2.imshow("foto3", img_median_blur)
    cv2.imshow("foto4", img_bilateral)
    cv2.waitKey(0)
    cv2.destroyAllWindows()