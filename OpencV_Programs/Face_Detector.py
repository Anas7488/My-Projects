import cv2
video_cap = cv2.VideoCapture(0)
face_cap = cv2.CascadeClassifier("/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-package/cv2/data/haarcascade_frontalface_alt.xml")
while True:
    ret , frame = video_cap.read()
    col = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces =  face_cap.detectMultiScale(col,1.1,4)
    cv2.imshow("Face Detector",frame)
    if cv2.waitKey(10) == ord("a"):
        break
    video_cap.release()