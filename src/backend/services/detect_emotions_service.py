from ai.detect_emotion_ai import EmotionAI
from models.emotions_model import EmotionModel

class EmotionService:
    @staticmethod
    def analyze_emotion(image_path):
        emotion = EmotionAI.detect_emotion(image_path)
        return EmotionModel.EMOTIONS.get(emotion, "Desconhecida")
