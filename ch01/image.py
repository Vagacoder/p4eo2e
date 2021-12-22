
# ! Example: Image processing, get pencil sketch using openCV-python
import cv2

# * read image file
img = cv2.imread("mm01.jpg")

# * process image
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# ? test 1: reverse -> blur -> reverse -> divide
rev_grey_img = 255 - grey_img
blur_r_g_img = cv2.GaussianBlur(rev_grey_img, (21,21), 0)
blur_g_img = 255 - blur_r_g_img

# ? test 2: blur -> divide
# blur_g_img = cv2.GaussianBlur(grey_img, (21, 21), 0)

# * get pencil sketch
pencil = cv2.divide(grey_img, blur_g_img, scale=255)

# * save to image files
# cv2.imwrite('bday_g.jpg', grey_img)
# cv2.imwrite('bday_r.jpg', rev_grey_img)
# cv2.imwrite('penci01.jpg', pencil)

# * show images
cv2.imshow("pencil", pencil)
cv2.imshow("blurred_grey_image", blur_g_img)
cv2.imshow("blurred_reversed_grey_image", blur_r_g_img)
cv2.imshow("reversed_grey_img", rev_grey_img)
cv2.imshow("grey_img", grey_img)
cv2.imshow("original", img)
cv2.waitKey(0)