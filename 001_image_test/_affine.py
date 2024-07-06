import cv2
import numpy as np
import utils.affine

def expand(image, ratio):
    h, w = image.shape[:2]
    src = np.array([[0.0, 0.0],[0.0, 1.0],[1.0, 0.0]], np.float32)
    dest = src * ratio
    dest[:,1] += 100 # シフトするピクセル値
    affine = cv2.getAffineTransform(src, dest)
    point = np.array([50,50,1]).reshape(-1,1)
    invet_affine = cv2.invertAffineTransform(affine)
    print('invert_affine',invet_affine)
    convert_matrx = np.block([[affine],[0,0,1]])
    invert_convert_matrx = np.block([[invet_affine],[0,0,1]])
    converted_point = np.dot(convert_matrx,point).astype(np.int64)
    print(converted_point)
    point2 = np.array([100,200,1]).reshape(-1,1)
    converted_point2 = np.dot(invert_convert_matrx,point2).astype(np.int64)
    print(converted_point2)
    tmp = cv2.warpAffine(image, affine, (2*w, 2*h + 200), cv2.INTER_LANCZOS4) # 補間法も指定できる
    tmp = cv2.circle(tmp, tuple(converted_point.flatten()[:2]), 5, (0, 0,0), -1)
    return tmp


dsize = (1500,800)
img = cv2.imread('res/dog.jpg')
# img = cv2.circle(img,(50,50), 25, (0,0,255), -1)
# img = expand(img,2.0)
affine_mat = utils.affine.get_scaling_image_affine(img.shape[:2][::-1],dsize)
point = np.array([100,100,1],dtype=np.float32).reshape(-1,1)
print(affine_mat)
print(np.dot(affine_mat,point))
img = cv2.warpAffine(img, affine_mat, dsize, cv2.INTER_LANCZOS4)
cv2.imshow('test',img)
cv2.waitKey()
