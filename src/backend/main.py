# main.py
import sys
sys.path.append('src')

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.controllers.emotion_controller import router as emotion_router

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],  
)

# Incluir as rotas
app.include_router(emotion_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
