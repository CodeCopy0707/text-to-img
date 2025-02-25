import torch
from flask import Flask, request, jsonify
from diffusers import DiffusionPipeline

app = Flask(__name__)

# Hugging Face Model Load
MODEL_NAME = "black-forest-labs/FLUX.1-dev"
pipe = DiffusionPipeline.from_pretrained(MODEL_NAME, torch_dtype=torch.float32)  # CPU mode
pipe.to("cpu")  # Render free tier ke liye CPU use karna padega

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    image = pipe(prompt).images[0]
    image.save("output.png")
    
    return jsonify({"message": "Image Generated Successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
