from PIL import Image
import numpy as np
'''
Prueba de numpy 
'''
im = np.array(Image.open('../resources/11838.jpg'))
im2 = np.array(Image.open('../resources/azul.jpg'))

cad = im2.shape
height = cad[0]
width = cad[1]

print(height)
print(width)

for i in range(height):
    for j in range(width):
        R, G, B = im2[i,j]
        if R <100 & G < 200 & B > 100:
            im2[i, j] = (0, 0, 0)

Image.fromarray(im2).save('../resources/output/save.jpg')


