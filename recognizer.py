from compreface import CompreFace
from config import get_config


class Recognizer:

    def __init__(self):
        self.config = None
        self.compre_face = None
        self.recognition_service = None
        self.face_collection = None

    def _get_config(self):
        if not self.config:
            self.config = get_config()["compreface"]
        return self.config

    def _get_compreface(self):
        if not self.compre_face:
            config = self._get_config()
            self.compre_face = CompreFace(config["url"], str(config["port"]))
        return self.compre_face

    def _get_recognition_service(self):
        if not self.recognition_service:
            config = self._get_config()
            self.recognition_service = self._get_compreface().init_face_recognition(config["recognition_api_key"])
        return self.recognition_service

    def _get_face_collection(self):
        if not self.face_collection:
            self.get_face_collection = self._get_recognition_service().get_face_collection()
        return self.face_collection

    def recognize_face(self, image):
        """
        Return the subject recognized (and verified) in the image, if any.
        Example format of returned subject as a dict:
        {
            "subject": "Grayson"
            "similarity": 0.9
        }
        Accepts an image file in the form of bytes.
        If no recognized face is present, returns None.
        """
        # Attempt to recognize known faces from the image
        faces = self._get_recognition_service().recognize(image)["result"]
        # If any known faces are detected, return true if the face meets the similarity threshold
        threshold = self._get_config()["similarity_threshold"]
        for face in faces:
            for subject in face["subjects"]:
                if subject["similarity"] >= threshold:
                    return subject
        return None
