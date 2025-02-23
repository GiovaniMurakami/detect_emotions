document
  .getElementById("uploadForm")
  .addEventListener("submit", async function (event) {
    event.preventDefault();

    const fileInput = document.getElementById("imageFile");
    if (!fileInput.files.length) {
      alert("Por favor, selecione uma imagem.");
      return;
    }

    const formData = new FormData();
    formData.append("file", fileInput.files[0]);

    try {
      const response = await fetch("http://127.0.0.1:8000/detect-emotion/", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        const errorData = await response.json();
        document.getElementById("emotionText").textContent =
          "Erro ao detectar a emoção.";
        document.getElementById("confidenceText").textContent =
          errorData.error || "Erro desconhecido";
        return;
      }

      const result = await response.json();
      const dominantEmotion = getDominantEmotion(result.emotions);

      document.getElementById(
        "emotionText"
      ).textContent = `Emoção dominante: ${dominantEmotion.name}`;
      document.getElementById(
        "confidenceText"
      ).textContent = `Confiança: ${dominantEmotion.score.toFixed(2)}%`;
    } catch (error) {
      document.getElementById("emotionText").textContent =
        "Erro na requisição.";
      document.getElementById("confidenceText").textContent =
        error.message || "Erro desconhecido";
    }
  });

function getDominantEmotion(emotions) {
  const emotionNames = Object.keys(emotions);
  let dominantEmotion = emotionNames[0];
  let highestScore = emotions[dominantEmotion];

  emotionNames.forEach((emotion) => {
    if (emotions[emotion] > highestScore) {
      dominantEmotion = emotion;
      highestScore = emotions[emotion];
    }
  });

  return { name: dominantEmotion, score: highestScore };
}
