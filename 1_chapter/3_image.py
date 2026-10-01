import cv2 as cv

img = cv.imread(r"images\i1.jpg")

img = cv.resize(img , (400, 500))

gry_img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("garu image",gry_img)
cv.imshow("image",img)
cv.waitKey(0)
cv.destroyAllWindows()