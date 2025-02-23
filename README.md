Aqui está o `README.md` completo, agora com a documentação do endpoint `/detect-emotion/` e sem mencionar o `/docs` (já que a rota não existe):

````markdown
# Projeto de Detecção de Emoções em Imagens

Este é um projeto de detecção de emoções em imagens, utilizando FastAPI e um modelo de aprendizado de máquina para análise de emoções a partir de imagens enviadas.

## Requisitos

Certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.10 ou superior
- pip
- virtualenv (opcional, mas recomendado)

## Instruções para Executar o Projeto

### Passo 1: Clonar o Repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/username/repository.git
cd repository
```
````

### Passo 2: Criar um Ambiente Virtual (opcional, mas recomendado)

Crie e ative um ambiente virtual para o projeto:

```bash
python3 -m venv venv
source venv/bin/activate  # No Windows use: venv\Scripts\activate
```

### Passo 3: Instalar Dependências

Instale todas as dependências do projeto:

```bash
pip install -r requirements.txt
```

### Passo 4: Executar o Servidor

Para rodar a aplicação, execute o seguinte comando:

```bash
PYTHONPATH=src uvicorn backend.main:app --reload
```

O servidor será iniciado em `http://127.0.0.1:8000`. Você pode acessar a documentação interativa da API utilizando a interface do **Swagger** em:

```
http://127.0.0.1:8000/docs
```

## Endpoints da API

### `POST /detect-emotion/`

Este endpoint recebe um arquivo de imagem e retorna as emoções detectadas na imagem.

#### Descrição

Este endpoint realiza a análise de emoções presentes em uma imagem, utilizando o serviço de detecção de emoções. Ele aceita um arquivo de imagem no formato `multipart/form-data` e retorna um JSON com as emoções detectadas.

#### Parâmetros

- **file** (corpo da requisição): O arquivo de imagem a ser analisado.
  - Tipo: `file`
  - Formato: Qualquer formato de imagem suportado (ex: PNG, JPEG).

#### Resposta

- **200 OK**: Se a análise for realizada com sucesso, a resposta será um JSON contendo as emoções detectadas.

  **Exemplo de resposta**:

  ```json
  {
    "emotions": {
      "happy": 0.85,
      "sad": 0.1,
      "surprise": 0.05
    }
  }
  ```

- **500 Internal Server Error**: Caso ocorra algum erro durante o processo de análise, o servidor retornará um erro com o detalhe do problema.

  **Exemplo de resposta**:

  ```json
  {
    "detail": "Erro ao processar a imagem"
  }
  ```

#### Exemplo de Requisição

Para testar o endpoint utilizando o `curl`, o seguinte comando pode ser usado:

```bash
curl --request POST \
  --url http://127.0.0.1:8000/detect-emotion \
  --header 'Accept: */*' \
  --header 'Accept-Language: en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7' \
  --header 'Connection: keep-alive' \
  --header 'Content-Type: multipart/form-data' \
  --header 'Origin: http://127.0.0.1:5500' \
  --header 'Referer: http://127.0.0.1:5500/' \
  --header 'Sec-Fetch-Dest: empty' \
  --header 'Sec-Fetch-Mode: cors' \
  --header 'Sec-Fetch-Site: same-site' \
  --header 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36' \
  --header 'sec-ch-ua: "Not(A:Brand";v="99", "Google Chrome";v="133", "Chromium";v="133"' \
  --header 'sec-ch-ua-mobile: ?0' \
  --header 'sec-ch-ua-platform: "Linux"' \
  --form file=@/home/giovani/Downloads/395e07ad-fe68-48a0-9aef-d96238860614.jpeg
```

### Documentação do Código (para desenvolvedores)

No código, o endpoint `/detect-emotion/` é registrado no **emotion_controller.py** e está configurado da seguinte forma:

```python
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
```

### Funcionalidade

1. O arquivo de imagem é recebido como um **UploadFile** através de uma requisição POST.
2. O conteúdo do arquivo é lido e passado para o serviço **EmotionService**, que realiza a análise das emoções.
3. As emoções são retornadas em um formato JSON.

Se o serviço de análise falhar, um erro `500` será lançado, e a mensagem de erro será retornada.

---

## Instalar Dependências

### Arquivo `requirements.txt`

Este projeto depende das seguintes bibliotecas, que podem ser instaladas com o comando `pip install -r requirements.txt`:

```
fastapi==0.95.0
uvicorn==0.22.0
tensorflow==2.11.0
numpy==1.23.3
opencv-python==4.6.0.66
```
