from recognizer import Recognizer


recognizer = Recognizer()

test_image = "test_images/grayson.jpg"

print("Attempting to recognize subjects from image: " + test_image)

subject = recognizer.recognize_face(test_image)

if subject is None:
    print("No subjects detected in image.")
else:
    print("Detected subject: " + subject["subject"] + " with similarity " + str(subject["similarity"]))