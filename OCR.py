import cv2
import os, io
from google.cloud import vision


def captureImage():
    cam = cv2.VideoCapture(0)
    cv2.namedWindow("Scanner")
    img_counter = 0
    while True:
        ret, frame = cam.read()
        if not ret:
            print("failed to grab frame")
            break
        cv2.imshow("test", frame)
        k = cv2.waitKey(1)
        if k % 256 == 27:
            print("Escape hit, closing...")
            break
        elif k % 256 == 32:
            img_name = "opencv_frame_{}.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    cam.release()
    cv2.destroyAllWindows()


def Detect_text():
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = r"/home/manu/Cap/Real_Time/VisionAPI_DEMO/ServiceAccountToken.json"
    client = vision.ImageAnnotatorClient()
    FILE_NAME = "opencv_frame_0.png"
    FOlDER_PATH = "/home/manu/Cap/Real_Time/"
    with io.open(os.path.join(FOlDER_PATH, FILE_NAME), 'rb') as image_file:
        context = image_file.read()

    image = vision.Image(content=context)

    response = client.document_text_detection(image=image)
    docText = response.full_text_annotation.text
    print(docText)
    pages = response.full_text_annotation.pages

    for page in pages:
        for block in page.blocks:
            print("block confidence", block.confidence)
            for paragraph in block.paragraphs:
                print("paragraph confidence", paragraph.confidence)

                for word in paragraph.words:
                    word_text = ''.join([symbol.text for symbol in word.symbols])

                    print("Word texxt : {0} (Condidence:{1}".format(word_text, word.confidence))

                    for symbol in word.symbols:
                        print('\tSymbol: {0} confidence:{1}'.format(symbol.text, symbol.confidence))


captureImage()
Detect_text()

