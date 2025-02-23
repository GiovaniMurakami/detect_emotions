# services/emotion_service.py

from deepface import DeepFace
import numpy as np
from PIL import Image
from io import BytesIO
from backend.models.emotion_model import EmotionModel

class EmotionService:
    @staticmethod
    def analyze_emotions(image_data):
        try:
            image = Image.open(BytesIO(image_data))
            image_np = np.array(image)

            analysis = DeepFace.analyze(image_np, actions=['emotion'])

            emotions = {emotion: float(value) for emotion, value in analysis[0]['emotion'].items()}
            return emotions
        
        except Exception as e:
            raise Exception(f"Erro ao processar a imagem: {str(e)}")
