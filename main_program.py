import numpy as np
import urllib.request
import array as arr
import Saturation
import InstagramScrap
from pprint import pprint
import cv2
import imutils
import Blue
import red
import Orange
import green
import Violet
import Yellow
import fullBody
import excelTest


k = InstagramScrap.InstagramScraper()
results = k.profile_page_recent_posts('https://www.instagram.com/madhavee_anthony/')
pprint(results)

urls = results
pprint(urls)
i=1
AvBlue = 0
AvGreen = 0
AvRed =0
AvOrange =0
AvViolet =0
AvYellow =0
AvSaturation =0
AvBrightness=0
AvgFaces=0
AvPeople=0
for url in urls:


    # download the image URL and display it

    print
    "downloading %s" % (url)
    print(i)
    image = InstagramScrap.url_to_image(url)
    #cv2.imshow("Image", image)
    image1 = imutils.resize(image, width=750)
    C = Saturation.image_colorfulnessss(image1)
    C=float(C)

    print("Saturation       :%f" %C)
    cv2.putText(image1, "Saturation:" "{:.2f}".format(C), (40, 40),
    cv2.FONT_HERSHEY_SIMPLEX, 1.4, (0, 255, 0), 3)
    #cv2.imshow("Saturation", image1)
    if image is None:
        print('Could not open or find the image: ')
        exit(0)
    new_image = np.zeros(image.shape, image.dtype)
    alpha = 2.0  # Simple contrast control
    beta = 0
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            for c in range(image.shape[2]):
                new_image[y, x, c] = np.clip(alpha * image[y, x, c] + beta, 0, 255)
    print("Image brightness :", np.clip(1.0 * image[y, x, c] + beta, 0, 255))
    B =np.clip(1.0 * image[y, x, c] + beta, 0, 255)
    ###########################################################################################
    face_cascade = cv2.CascadeClassifier(
        'E:/FYP/openCV/Counting-number-of-faces-in-a-picture-using-python-opencv-master/haarcascade_frontalface_alt.xml')
   # img = cv2.imread('E:\FYP\openCV\Counting-number-of-faces-in-a-picture-using-python-opencv-master\eee.jpg')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    print("Number of faces  : %d"%len(faces))
    F=len(faces)
    print("Number of people : %d"%fullBody.body_detect(image))
    fullBody.body_detect(image)
    s1 = "E:\FYP\openCV\Hue\ColorDetect/ColorSource.jpg"
    urllib.request.urlretrieve(url, s1)
    print("Blue percentage  : %.2f" % Blue.blue_Count())
    print("Red percentage   : %.2f" % red.red_Count())
    print("Green percentage : %.2f" % green.green_Count())
    print("Yellow percentage: %.2f" % Yellow.yellow_Count())
    print("Orange percentage: %.2f" % Orange.Orange_Count())
    print("Violet percentage: %.2f" % Violet.violet_Count())
    cv2.waitKey(1)
    AvBlue = AvBlue + Blue.blue_Count()
    AvGreen = AvGreen + green.green_Count()
    AvOrange = AvOrange + Orange.Orange_Count()
    AvRed = AvRed + red.red_Count()
    AvViolet = AvViolet + Violet.violet_Count()
    AvYellow = AvYellow + Yellow.yellow_Count()
    AvgFaces = AvgFaces + len(faces)
    AvPeople= AvPeople + fullBody.body_detect(image)
    AvSaturation = AvSaturation + C
    AvBrightness = AvBrightness + B
    i=i+1
    print()
i=i-1
print ()
print ("Number of Images:%d"%i)

print("Average Blue percentage  =%f"%(AvBlue/i))
print("Average Green percentage =%f"%(AvGreen/i))
print("Average Red percentage   =%f"%(AvRed/i))
print("Average Yellow percentage=%f"%(AvYellow/i))
print("Average Violet percentage=%f"%(AvViolet/i))
print("Average Orange percentage=%f"%(AvOrange/i))
print("Average number of faces  =%f"%(AvgFaces/i))
print("Average number of people =%f"%(AvPeople/i))
print("Average Saturation       =%f"%(AvSaturation/i))
print("Average Brightness       =%f"%(AvBrightness/i))
#a=[]
#a=arr.array[AvSaturation,AvBrightness,AvgFaces,AvPeople,AvBlue,AvGreen,AvRed,AvOrange,AvYellow,AvViolet]
excelTest.writeCell([AvSaturation/i,AvBrightness/i,AvgFaces/i,AvPeople/i,AvBlue/i,AvGreen/i,AvRed/i,AvOrange/i,AvYellow/i,AvViolet/i])


