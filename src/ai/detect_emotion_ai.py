from deepface import DeepFace
import cv2

class EmotionAI:
    @staticmethod
    def detect_emotion(image_path):
        try:
            print(f"Analisando imagem: {image_path}")
            result = DeepFace.analyze(image_path, actions=['emotion'])
            print(f"Resultado da análise: {result}")
            return result[0]['dominant_emotion']
        except Exception as e:
            print(f"Erro na análise: {str(e)}")
            return f"Erro na análise: {str(e)}"

