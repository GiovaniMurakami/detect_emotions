from services.detect_emotions_service import EmotionService

class EmotionController:
    @staticmethod
    def process_image(image_path):
        emotion = EmotionService.analyze_emotion(image_path)
        print(f"Emoção detectada: {emotion}")
