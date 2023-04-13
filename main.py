import image_download
from firebase_connecting import firebase_connectings
from recognition import FaceRecognition

if __name__ == '__main__':
    #MAIN FUNCTION
    print('Main Function')




    #to download the images from firebase
    #image_download.image_downloads()


    #firebase_connectings("95072015015")

    #face recoginiton process
    fr = FaceRecognition()
    fr.run_recognition()
