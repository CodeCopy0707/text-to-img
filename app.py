from flask import Flask, request, jsonify, send_file
import torch
from diffusers import StableDiffusionPipeline
import os

app = Flask(__name__)

# Model Load (Lightweight Version)
model_id = "runwayml/stable-diffusion-v1-5"
pipe = StableDiffusionPipeline.from_pretrained(model_id, torch_dtype=torch.float16)
device = "cuda" if torch.cuda.is_available() else "cpu"
pipe.to(device)

@app.route('/generate', methods=['POST'])
def generate_image():
    try:
        data = request.get_json()
        prompt = data.get("prompt", "")

        if not prompt:
            return jsonify({"error": "Prompt is required"}), 400

        image = pipe(prompt).images[0]
        image_path = "generated_image.png"
        image.save(image_path)

        return send_file(image_path, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
