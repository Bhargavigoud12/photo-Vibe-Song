from deepface import DeepFace

def detect_emotion(image_path: str) -> str:
    """Analyze the image and return the dominant emotion."""
    result = DeepFace.analyze(img_path=image_path, actions=['emotion'], enforce_detection=False)
    return result[0]['dominant_emotion']