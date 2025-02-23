# controllers/emotion_controller.py

from fastapi import HTTPException, APIRouter, File, UploadFile
from backend.services.emotion_service import EmotionService
from fastapi.responses import JSONResponse

router = APIRouter()

@router.post("/detect-emotion/")
async def detect_emotion(file: UploadFile = File(...)):
    try:
        # Obter os dados da imagem
        image_data = await file.read()

        # Utilizar o serviço para analisar as emoções
        emotions = EmotionService.analyze_emotions(image_data)

        # Retornar o resultado
        return JSONResponse(content={"emotions": emotions})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
