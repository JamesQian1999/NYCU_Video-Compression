import numpy as np
from PIL import Image
import time
from tqdm import tqdm

def C(x):
    if(x):
        return 1
    return 1./np.sqrt(2)

def DCT_1d(input):

    dct_1d = np.zeros(input.shape)
    N      = input.shape[0]
    for u in range(N):
        sum = 0
        for x in range(N):
            sum += input[x] * np.cos((2*x+1) * u * np.pi/(2*N))
        dct_1d[u] = sum * C(u) * np.sqrt(2/N)

    return dct_1d


def IDCT_1d(input):
    idct_1d = np.zeros(input.shape)

    for x in range(N):
        sum = 0
        for u in range(N):
            sum += C(u) * input[u] * np.cos((2*x+1) * u * np.pi/(2*N))
        idct_1d[x] = sum * np.sqrt(2/N)

    return idct_1d

def DCT(img):
    dct = np.zeros(image.shape)
    for i in tqdm(range(r), desc="dct_1d_x"):
        dct[i,:] = DCT_1d( img[i,:])

    for i in tqdm(range(r), desc="dct_1d_y"):
        dct[:,i] = DCT_1d( dct[:,i])

    return dct

def IDCT(img):
    idct = np.zeros(image.shape)
    for i in tqdm(range(r), desc="idct_1d_y"):
        idct[:,i] = IDCT_1d(img[:,i])
    for i in tqdm(range(r), desc="idct_1d_x"):
        idct[i,:] = IDCT_1d(  idct[i,:])

    return idct

if __name__ == "__main__":
    # input image
    img = Image.open('lena.png')
    img = img.convert('L')
    h, w = img.size
    r = 128
    img = img.resize((int(r), int(r)))
    image = np.asarray(img)
    N = image.shape[0]

    #dct 1d
    fp = open('report_1d.txt', 'w')
    dct_1d = np.zeros(image.shape)
    start = time.process_time()
    for i in tqdm(range(r), desc="dct_1d_x"):
        dct_1d[i,:] = DCT_1d( image[i,:])

    for i in tqdm(range(r), desc="dct_1d_y"):
        dct_1d[:,i] = DCT_1d(dct_1d[:,i])
    end = time.process_time()

    np.save('dct_1d', dct_1d)
    fp.write(f"dct time: {end - start} s\n")

    idct_1d = np.zeros(image.shape)
    start = time.process_time()
    for i in tqdm(range(r), desc="idct_1d_y"):
        idct_1d[:,i] = IDCT_1d(dct_1d[:,i])
    for i in tqdm(range(r), desc="idct_1d_x"):
        idct_1d[i,:] = IDCT_1d(  idct_1d[i,:])
    end = time.process_time()

    np.save('idct_1d', idct_1d)
    fp.write(f"idct time: {end - start} s\n")
