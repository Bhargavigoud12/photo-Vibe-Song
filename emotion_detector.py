<<<<<<< HEAD
from deepface import DeepFace

def detect_emotion(image_path: str) -> str:
    """Analyze the image and return the dominant emotion."""
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
=======
from deepface import DeepFace

def detect_emotion(image_path: str) -> str:
    """Analyze the image and return the dominant emotion."""
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
>>>>>>> 85c14a2a8ec9826ddfaf297010631cb5c821f1ca
    return result[0]['dominant_emotion']