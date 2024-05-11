from flask import render_template, request
import requests
import os
from io import BytesIO  # Import BytesIO from io module
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

def index():
    return render_template("index.html", caption="")

def describe():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    image_url = request.form["image_url"]

    # Download image from URL
    response = requests.get(image_url)
    image = Image.open(BytesIO(response.content)).convert('RGB')

    inputs = processor(image, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    return render_template("index.html", image=image_url, caption=caption)
