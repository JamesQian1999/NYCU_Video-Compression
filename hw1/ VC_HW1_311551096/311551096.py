# Student ID: 311551096
# Date      : 2023/03/01


# Output 8 grayscale images representing R, G, B, Y, U, V, Cb, Cr, respectively
import numpy as np
from PIL import Image

# Read image
img = Image.open('lena.png')
data = np.asarray(img)

R = data[:,:,0]
G = data[:,:,1]
B = data[:,:,2]
# Write R,G,B image
Image.fromarray(R).save('lena_R.png')
Image.fromarray(G).save('lena_G.png')
Image.fromarray(B).save('lena_B.png')

Y = R *  0.299 + G *  0.587 + B *  0.114
U = R * -0.169 + G * -0.331 + B *  0.500 + 128
V = R *  0.500 + G * -0.419 + B * -0.081 + 128
# Write Y,U,V image
Image.fromarray(np.uint8(Y)).save('lena_Y.png')
Image.fromarray(np.uint8(U)).save('lena_U.png')
Image.fromarray(np.uint8(V)).save('lena_V.png')

Cb = R * -0.168736 + G * -0.331264 + B *  0.500000 + 128
Cr = R *  0.500000 + G * -0.418688 + B * -0.081312 + 128
# Write Cb,Cr image
Image.fromarray(np.uint8(Cb)).save('lena_Cb.png')
Image.fromarray(np.uint8(Cr)).save('lena_Cr.png')