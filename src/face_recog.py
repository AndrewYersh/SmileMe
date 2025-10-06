from PIL import Image, ImageDraw
import face_recognition

if __name__ == "__main__":
    print(face_recognition.__version__)
    print(face_recognition.__file__)

    # Load the jpg file into a numpy array
    image = face_recognition.load_image_file("test_images/group_1.jpg")

    # Find all facial features in all the faces in the image
    face_landmarks_list = face_recognition.face_landmarks(image, model='large')
    
    print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

    # Create a PIL imagedraw object so we can draw on the picture
    pil_image = Image.fromarray(image)
    d = ImageDraw.Draw(pil_image)

    for face_landmarks in face_landmarks_list:
        # Let's trace out each facial feature in the image with a line!
        for facial_feature in face_landmarks.keys():
            d.line(face_landmarks[facial_feature], width=5)
    top_lip_points = face_landmarks_list[0]['top_lip']
    bottom_lip_points = face_landmarks_list[0]['bottom_lip']
    # Show the picture  
    pil_image.show()

