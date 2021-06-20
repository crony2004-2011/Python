import os
os.chdir(r"C:\Users\hp\Desktop\opencv")
import cv2
import face_recognition
import matplotlib.pyplot as plt

img1 = face_recognition.load_image_file("suspect2.jpg")
img1 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)
img2 = face_recognition.load_image_file("suspect3.jpg")
img2 = cv2.cvtColor(img1, cv2.COLOR_BGR2RGB)

#loc will give face locations 4 points
loc = face_recognition.face_locations(img1)[0]
#encodeloc gives 128 different dimensions of the face within the image
encodeloc = face_recognition.face_encodings(img1)[0]
cv2.rectangle(img1, (loc[3], loc[0]), (loc[1], loc[2]),(255,0), 2)

#loc1
loc1 = face_recognition.face_locations(img2)[0]
encodeloc1 = face_recognition.face_encodings(img2)[0]
cv2.rectangle(img2, (loc1[3],loc1[0]),(loc1[1],loc1[2]),(255,0),2)
#print(encodeloc,encodeloc1)

#NOW WE MATCH FACE IN img1 to another image
match = face_recognition.compare_faces([encodeloc], encodeloc1)
face_dis = face_recognition.face_distance([encodeloc1],encodeloc)
#print(match, face_dis)
#cv2.putText(img1, "{}-{}".format(match,face_dis[0]),(50,50), cv2.FONT_HERSHEY_COMPLEX,1,(0,255,255), 2)
#cv2.imshow('face', img1)
#cv2.waitKey(0)


