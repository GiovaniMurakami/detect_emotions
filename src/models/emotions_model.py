class EmotionModel:
    EMOTIONS = {
        "angry": "Raiva",
        "disgust": "Nojo",
        "fear": "Medo",
        "happy": "Feliz",
        "neutral": "Neutro",
        "sad": "Triste",
        "surprise": "Surpresa"
    }
    
    @classmethod
    def get_emotions(cls):
        return cls.EMOTIONS
