import cv2
import os

"""Setup directories needed"""
def setupFolders():
	listOfFolders = ["data","positives","negatives"]
	for folder in listOfFolders:
		if not os.path.exists(folder):
			os.makedirs(folder)
		else:
			print("Warning: One of the folders already exists.")
			exit()

"""Generates negative images from a source solder"""
def getAndResizeImages(path="images", imgNumber=1000):
    count = 0
    for imgFile in os.listdir(path):
        # need to include gray scale
        img = cv2.imread(os.path.join(path, imgFile)) #assuming gray scale imgs in source folder
        imgResize = cv2.resize(img, (100, 100))
        if not os.path.exists("negatives"):
            os.mkdir("negatives")
        cv2.imwrite("negatives/" + str(count) + ".jpg", imgResize)
        count += 1
        if count > imgNumber:
            break

"""Generates a negative images map, which is required by CV2 to generate samples"""
def createNegatives():
    for folder in os.listdir():
        if (folder == "negatives"):
            for img in os.listdir(folder):
                toWrite = folder + "/" + img + "\n"
                with open("negativesMap.txt", 'a') as handle:
                    handle.write(toWrite)
