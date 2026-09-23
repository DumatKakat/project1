import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import os
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
# from mediapipe.python.solutions import hands as mp_hands
import shutil

def readImage():
    root = os.getcwd()
    imgPath = ".\\img\\Udin_din_din_din_dun.jpg"
    # imgPath = str(imgPath, encoding="utf-8")
    img = cv.imread(imgPath)
    cv.imshow("Image", img)
    cv.waitKey(0)

def writeImage():
    root = os.getcwd()
    imgPath = ".\\img\\Udin_din_din_din_dun.jpg"
    img = cv.imread(imgPath)
    output = ".\\img\\Udin.jpg"
    # cv.imshow("Image", img)
    cv.imwrite(output, img)

def videoFromWebcam():
    cap = cv.VideoCapture(0)

    if not cap.isOpened():
        exit()

    while True:
        ret, frame = cap.read()
        if ret: 
            cv.imshow("Webcam", frame)
        
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    cv.destroyAllWindows()

def videoFromFile():
    path = ".\\video\\Los Pingüinos x Last Christmas.mp4"
    cap = cv.VideoCapture(path)

    while cap.isOpened():
        ret, frame = cap.read()
        cv.imshow('video', frame)
        delay = int(1000/60)
        if cv.waitKey(delay) == ord('q'):
            break

def writeVideoToFile():
    cap = cv.VideoCapture(0)

    fourcc = cv.VideoWriter_fourcc(*'XVID')

    outPath = ".\\video\\webcsm.avi"

    out = cv.VideoWriter(outPath, fourcc, 20.0, (640, 480))

    while cap.isOpened():
        ret, frame = cap.read()
        if ret: 
            out.write(frame)
            cv.imshow("Webcam", frame)
        
        if cv.waitKey(1) == ord('q'):
            break

    cap.release()
    out.release()
    cv.destroyAllWindows()

def readAndWritePixel():
    imgPath = ".\\img\\Udin_din_din_din_dun.jpg"
    img = cv.imread(imgPath)
    imgRBG = cv.cvtColor(img, cv.COLOR_BGR2RGB)

    plt.figure()
    plt.imshow()
    plt.show()

def pureColor():
    zeros = np.zeros((100,100))
    ones = np.ones((100,100))
    bImg = cv.merge((zeros,zeros,255*ones))
    gImg = cv.merge((zeros,255*ones,zeros))
    rImg = cv.merge((255*ones,zeros,zeros))

    plt.figure()
    plt.subplot(231)
    plt.imshow(bImg)

    plt.subplot(232)
    plt.imshow(gImg)

    plt.subplot(233)
    plt.imshow(rImg)
    plt.show()

def bgrChanelGrayscale():
    path = ".\\img\\Udin.jpg"
    img = cv.imread(path)
    b,g,r = cv.split(img)

    plt.figure()
    plt.subplot(131)
    plt.imshow(b, cmap="gray")
    plt.subplot(132)
    plt.imshow(g, cmap="gray")
    plt.subplot(133)
    plt.imshow(r, cmap="gray")

    plt.show()

def bgrChannelColor():
    path = ".\\img\\Udin.jpg"
    img = cv.imread(path)
    b,g,r = cv.split(img)

    zeros = np.zeros_like(b)
    bImg = cv.merge((b,zeros,zeros))
    gImg = cv.merge((zeros,g,zeros))
    rImg = cv.merge((zeros,zeros,r))

    plt.figure()
    plt.subplot(131)
    plt.imshow(bImg)
    plt.subplot(132)
    plt.imshow(gImg)
    plt.subplot(133)
    plt.imshow(rImg)

    plt.show()

def grayScale():
    path = ".\\img\\Udin.jpg"
    img = cv.imread(path)

    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    cv.imshow("gray", imgGray)
    cv.waitKey(0)

def hsvColorSegment():
    path = ".\\img\\Udin.jpg"
    img = cv.imread(path)
    imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    lowerBound = np.array([0,0,0])
    upperBound = np.array([20,300,150])

    mask = cv.inRange(imgHSV, lowerBound, upperBound)

    plt.figure()
    plt.imshow(imgRGB)
    plt.show()

    cv.imshow('mask', mask)
    cv.waitKey(0)

def eyeMashine():
    cap = cv.VideoCapture(0)

    face_cascade = cv.CascadeClassifier('.venv\\Lib\\site-packages\\cv2\\data\\' + 'haarcascade_frontalface_default.xml')

    eye_cascade = cv.CascadeClassifier('.venv\\Lib\\site-packages\\cv2\\data\\' + 'haarcascade_eye.xml')

    print(cv.CascadeClassifier.empty(face_cascade))
    print(cv.CascadeClassifier.empty(eye_cascade))

    while True:
        ret, frame = cap.read()

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:
            cv.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 5)
            roi_gray  = gray[y:y+w, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.3, 5)
            for (ex,ey,ew,eh) in eyes:
                cv.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

        cv.imshow("Webcam", frame)

        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()


def count_fingers(landmarks):
    """Функция подсчета поднятых пальцев"""
    tip_ids = [4, 8, 12, 16, 20]  # ID кончиков пальцев
    fingers = []

    # Большой палец
    if landmarks[tip_ids[0]][0] > landmarks[tip_ids[0] - 1][0]:
        fingers.append(1)
    else:
        fingers.append(0)

    # Остальные пальцы
    for id in range(1, 5):
        if landmarks[tip_ids[id]][1] < landmarks[tip_ids[id] - 2][1]:
            fingers.append(1)
        else:
            fingers.append(0)

    return sum(fingers)

def eyeMashineHand():

    print(dir(mp.tasks.components))
    mp_draw = mp.solutions.drawing_utils
    mpHands = mp.solutions.hands
    hands = mpHands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.5)


    cap = cv.VideoCapture(0)

    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            continue

        frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        frameRGB.flags.writeable = False
        results = hands.process(frameRGB)
        frameRGB.flags.writeable = True
        frame = cv.cvtColor(frame, cv.COLOR_RGB2BGR)
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(
                    frame, hand_landmarks, mpHands.HAND_CONNECTIONS,
                    mp_draw.DrawingSpec(color=(0, 0, 255), circle_radius=5, thickness=2),
                    mp_draw.DrawingSpec(color=(0, 255, 0), thickness=2),)

                landmarks = []

                for lm in hand_landmarks.landmark:
                    h,w,c = frame.shape
                    cx,cy = int(lm.x*w), int(lm.y*h)
                    landmarks.append([cx,cy])

                fingers_up = count_fingers(landmarks)
                cv.putText(frame, f"Fingers : {fingers_up}", (10,30), cv.FONT_HERSHEY_SIMPLEX,1,(255,0,0), 2)

        cv.imshow("Webcam", frame)
        if cv.waitKey(1) == ord('q'):
            break
    cap.release()
    cv.destroyAllWindows()

if __name__ == "__main__":
    eyeMashineHand()
    print(cv.__version__)
