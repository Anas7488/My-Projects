import cv2
face_cascade = cv2.CascadeClassifier("//Library//Frameworks//Python.framework//Versions//3.12//lib//python3.12//site-packages//cv2//data//haarcascade_frontalface_alt.xml")
cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces =  face_cascade.detectMultiScale(gray,1.1,4)
    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(225,0,0),2)
        cv2.imshow("Face_Detector",frame)
        if cv2.waitKey(10) == ord('a'):
            break
        cap.release()