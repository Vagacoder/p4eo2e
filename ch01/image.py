import cv2

img = cv2.imread("bday.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
rev_grey_img = 255 - grey_img
blur_r_g_img = cv2.GaussianBlur(rev_grey_img, (21,21), 0)
blur_g_img = 255 - blur_r_g_img
pencil = cv2.divide(grey_img, blur_g_img, scale=25)

# cv2.imwrite('bday_g.jpg', grey_img)
# cv2.imwrite('bday_r.jpg', rev_grey_img)

# cv2.imshow("original", img)
# cv2.imshow("grey_img", grey_img)
# cv2.imshow("reversed_grey_img", rev_grey_img)
cv2.imshow("blurred_reversed_grey_image", blur_r_g_img)
cv2.imshow("blurred_grey_image", blur_g_img)
cv2.imshow("pencil", pencil)
cv2.waitKey(0)