import os
import sys

try:
    from PIL import Image
except ImportError:
    print("Pillow is not installed. Please install it with 'pip install Pillow'")
    sys.exit(1)

def create_thumbnail(input_path, output_path, size=(600, 400)):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    try:
        with Image.open(input_path) as img:
            img.thumbnail(size)
            img.save(output_path, "WEBP", quality=80)
            print(f"Created {output_path} (Size: {os.path.getsize(output_path) / 1024:.2f} KB)")
    except Exception as e:
        print(f"Error processing {input_path}: {e}")

images = [
    "images/otherParts/Basil construction/JPEG/lighting_1 - Photo.jpg",
    "images/otherParts/Gad apartment/JPEG/2025 gad_1 - Photo.jpg",
    "images/otherParts/James/JPEG/James HD_1 - Photo.jpg",
    "images/otherParts/PL 2025/JPEG/1.jpg",
    "images/otherParts/alphonse Fdg/JPEG/1 - Photo.jpg",
    "images/otherParts/jmv karumuna/9_1 - Photo.jpg",
    "images/otherParts/papa edith/JPEG/Papa edith bosco_1 - Photo.jpg",
    "images/otherParts/remera project/JPEG/Remera project_1 - Photo.jpg"
]

for img_path in images:
    if not os.path.exists(img_path):
        print(f"File not found: {img_path}")
        continue
    
    filename = os.path.basename(img_path)
    name_without_ext = os.path.splitext(filename)[0]
    output_path = os.path.join("images", "thumbnails", f"{name_without_ext}.webp")
    create_thumbnail(img_path, output_path)
