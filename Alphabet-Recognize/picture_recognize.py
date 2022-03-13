import cv2
# a text recognize library
from pytesseract import pytesseract

# command used in terminal to call tesseract
# 	for Windows, "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
# 	for Linux, "tesseract"
pytesseract.tesseract_cmd = "tesseract"

# read image from file
#img = cv2.imread('T.png')
#img = cv2.imread('k.png')
img = cv2.imread('TDK.png')
height, width, c = img.shape

# detect words in image and print
words_in_image = pytesseract.image_to_string(img)
print(words_in_image)

# detect words and boxes in image
letter_boxes = pytesseract.image_to_boxes(img)
#print(letter_boxes)
for box in letter_boxes.splitlines():
	box = box.split()
	x, y, w, h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
	cv2.rectangle(img, (x, height - y), (w, height - h), (0, 0, 255), 3)
	cv2.putText(img, box[0], (x, height - h + 32), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)

cv2.imshow("window", img)
cv2.waitKey(0)