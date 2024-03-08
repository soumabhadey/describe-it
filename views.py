from flask import render_template, request, url_for
import os
from PIL import Image
import tempfile
from transformers import BlipProcessor, BlipForConditionalGeneration




def index():
    return render_template("index.html", caption="")




def describe():
    processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

    image = request.files["image"]

    # temp_dir = tempfile.mkdtemp()
    static_dir = os.path.join(os.path.dirname(__file__), 'static')
    image_path = os.path.join(static_dir, image.filename)
    image.save(image_path)

    raw_image = Image.open(image).convert('RGB')

    inputs = processor(raw_image, return_tensors="pt")

    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)

    image_path = os.path.join("static", image.filename)

    return render_template("index.html", image=image_path, caption=caption)