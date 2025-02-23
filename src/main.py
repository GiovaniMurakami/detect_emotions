import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from controllers.detect_emotions_controller import EmotionController

def main():
    image_path = "src/fotos/teste1.jpeg"
    EmotionController.process_image(image_path)

if __name__ == "__main__":
    main()
