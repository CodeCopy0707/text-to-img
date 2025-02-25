import torch
from flask import Flask, request, jsonify
from diffusers import DiffusionPipeline

app = Flask(__name__)

# Hugging Face Model Load (DeepFloyd IF-I-M-v1.0)
MODEL_NAME = "DeepFloyd/IF-I-M-v1.0"
pipe = DiffusionPipeline.from_pretrained(
    MODEL_NAME, 
    variant="fp16", 
    torch_dtype=torch.float16
)

pipe.to("cpu")  # CPU mode for free-tier compatibility

@app.route("/generate", methods=["POST"])
def generate():
    data = request.json
    prompt = data.get("prompt", "")

    # Encode prompt
    prompt_embeds, negative_embeds = pipe.encode_prompt(prompt)

    # Generate Image
    generator = torch.manual_seed(0)
    image = pipe(
        prompt_embeds=prompt_embeds,
        negative_prompt_embeds=negative_embeds,
        generator=generator,
        output_type="pil"
    ).images[0]

    image.save("output.png")
    
    return jsonify({"message": "Image Generated Successfully!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
