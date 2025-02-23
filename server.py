from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO
from PIL import Image
import numpy as np
from deepface import DeepFace
from fastapi.responses import JSONResponse

app = FastAPI()

# Adicionando CORS para todas as origens
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP
    allow_headers=["*"],  # Permite todos os cabeçalhos
)

@app.post("/detect-emotion/")
async def detect_emotion(file: UploadFile = File(...)):
    # Ler a imagem
    image_data = await file.read()
    image = Image.open(BytesIO(image_data))

    # Converter a imagem para o formato que o DeepFace espera
    image_np = np.array(image)

    try:
        # Processamento de emoções usando o DeepFace
        analysis = DeepFace.analyze(image_np, actions=['emotion'])

        # Convertendo os valores para float antes de retornar
        emotions = {emotion: float(value) for emotion, value in analysis[0]['emotion'].items()}

        # Retornar o resultado
        return JSONResponse(content={"emotions": emotions})

    except Exception as e:
        return JSONResponse(content={"error": str(e)}, status_code=500)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
