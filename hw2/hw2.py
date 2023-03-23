import numpy as np
from PIL import Image
import time
from tqdm import tqdm

def C(x):
    if(x):
        return 1
    return 1./np.sqrt(2)


# input image
img = Image.open('lena.png')
img = img.convert('L')
h, w = img.size
r = 256
img = img.resize((int(r), int(r)))
image = np.asarray(img)
N = image.shape[0]


#dct 1d
fp = open('report_1d.txt', 'w')

def DCT_1d(input):

    dct_1d = np.zeros(input.shape)
    N      = input.shape[0]
    for u in range(N):
        sum = 0
        for x in range(N):
            sum += input[x] * np.cos((2*x+1) * u * np.pi/(2*N))
        dct_1d[u] = sum * C(u) * np.sqrt(2/N)

    return dct_1d


dct_1d = np.zeros(image.shape)
start = time.process_time()
for i in tqdm(range(r), desc="dct_1d_x"):
    dct_1d[i,:] = DCT_1d( image[i,:])

for i in tqdm(range(r), desc="dct_1d_y"):
    dct_1d[:,i] = DCT_1d(dct_1d[:,i])
end = time.process_time()

np.save('dct_1d', dct_1d)
fp.write(f"dct time: {end - start} s\n")



def IDCT_1d(input):
    idct_1d = np.zeros(input.shape)

    for x in range(N):
        sum = 0
        for u in range(N):
            sum += C(u) * input[u] * np.cos((2*x+1) * u * np.pi/(2*N))
        idct_1d[x] = sum * np.sqrt(2/N)

    return idct_1d

idct_1d = np.zeros(image.shape)
start = time.process_time()
for i in tqdm(range(r), desc="idct_1d_y"):
    idct_1d[:,i] = IDCT_1d(dct_1d[:,i])
for i in tqdm(range(r), desc="idct_1d_x"):
    idct_1d[i,:] = IDCT_1d(  idct_1d[i,:])
end = time.process_time()

np.save('idct_1d', idct_1d)
fp.write(f"idct time: {end - start} s\n")



# dct 2d
fp = open('report_2d.txt', 'w')

start = time.process_time()
dct_2d = np.zeros(image.shape)
for u in tqdm(range(N), desc="dct_2d"):
    for v in tqdm(range(N), leave = False):
        sum = 0
        for x in range(N):
            for y in range(N):
                sum += image[x][y] * np.cos((2*x+1) * u * np.pi/(2*N)) * np.cos((2*y+1) * v * np.pi/(2*N))
        dct_2d[u][v] = sum * C(u) * C(v) * 2/N
end = time.process_time()

np.save('dct_2d', dct_2d)
fp.write(f"dct time: {end - start} s\n")


start = time.process_time()
idct_2d = np.zeros(image.shape)
for x in tqdm(range(N), desc="idct_2d"):
    for y in tqdm(range(N), leave = False):
        sum = 0
        for u in range(N):
            for v in range(N):
                sum += C(u) * C(v) * dct_2d[u][v] * np.cos((2*x+1) * u * np.pi/(2*N)) * np.cos((2*y+1) * v * np.pi/(2*N))
        idct_2d[x][y] = sum * 2/N
end = time.process_time()

np.save('idct_2d', idct_2d)
fp.write(f"idct time: {end - start} s\n")
