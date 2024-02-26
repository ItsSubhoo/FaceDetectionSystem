import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
while True:
    _, ppl = cap.read()
    gray = cv2.cvtColor(ppl, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 11.4, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(ppl, (x, y), (x+w, y+h), (255, 155, 0), 2)
    cv2.imshow('FacialDetection', ppl)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
