import os
import cv2
from deepface.detectors.detector_ssd import FaceDetectorSSDMobilenetV2


def test_ssd():
    face_detector = FaceDetectorSSDMobilenetV2()
    test_image = cv2.imread(image, cv2.IMREAD_COLOR)
    faces = face_detector.detect(test_image)

    for face in faces:
      cv2.rectangle(test_image,(int(face.x),int(face.y)),(int(face.x + face.w), int(face.y + face.h)), (0,255,0),3)

    window_name = "image"
    cv2.namedWindow(window_name, cv2.WND_PROP_AUTOSIZE)
    cv2.startWindowThread()

    cv2.imshow('image', test_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    cv2.waitKey(1)
    print("done showing face annotated image!")

    for face in faces:
      print(face.face_landmark)

    print("done")


def test_ssd_webcam():
    cap = cv2.VideoCapture(0) 


    face_detector = FaceDetectorSSDMobilenetV2()
    while(True):
        ret, frame = cap.read()

        test_image = frame
        faces = face_detector.detect(test_image)

        for face in faces:
          cv2.rectangle(test_image,(int(face.x),int(face.y)),(int(face.x + face.w), int(face.y + face.h)), (0,255,0),3)

        window_name = "image"
        cv2.namedWindow(window_name, cv2.WND_PROP_AUTOSIZE)
        cv2.startWindowThread()



        cv2.imshow(window_name, test_image)

        if cv2.waitKey(5) & 0xFF == ord('q'):
            break

    cap.release()


    cv2.destroyAllWindows()


if __name__ == "__main__":
    test_ssd_webcam()
