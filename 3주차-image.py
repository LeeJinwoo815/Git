import cv2

fname = "Lighthouse.jpg"
img_gray = cv2.imread(fname, 0)
img_color = cv2.imread(fname, 1)

h_new = img_gray.shape[0]//3 
w_new = img_gray.shape[1]//2 
img_gnew = cv2.resize(img_gray, (w_new, h_new))
img_cnew = cv2.resize(img_color, (w_new, h_new))


cv2.imshow('Gray', img_gnew)
cv2.imshow('Color', img_cnew)

fname_new = "Lighthouse_resized.jpg"
cv2.imwrite(fname_new, img_cnew)
cv2.waitKey(2000) 
cv2.destroyAllWindows()

from glob import glob
glob('3주차 image.py')



