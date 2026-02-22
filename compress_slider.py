import os
from PIL import Image

def resize_slider_image(input_path, output_path, max_width=1920):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with Image.open(input_path) as img:
            # Calculate new height maintaining aspect ratio
            width, height = img.size
            if width > max_width:
                new_height = int(max_width * height / width)
                img = img.resize((max_width, new_height), Image.Resampling.LANCZOS)
            
            # Convert RGBA to RGB if saving as JPEG (or keep for WEBP)
            # Webp can handle RGBA but we'll convert to RGB for consistency unless transparent
            if img.mode in ('RGBA', 'P'):
                img = img.convert('RGB')
                
            img.save(output_path, "WEBP", quality=85)
            print(f"Saved {output_path} ({os.path.getsize(output_path) / 1024:.2f} KB)")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

images = [
    ("images/forSlider/slide1.png", "images/thumbnails/slider_1.webp"),
    ("images/forSlider/slide2.jpg", "images/thumbnails/slider_2.webp"),
    ("images/forSlider/slide3.jpg", "images/thumbnails/slider_3.webp")
]

for src, dst in images:
    if os.path.exists(src):
        resize_slider_image(src, dst)
    else:
        print(f"File not found: {src}")
