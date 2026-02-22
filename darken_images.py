import os
from PIL import Image, ImageEnhance

images_to_darken = [
    "images/thumbnails/slider_2.webp",
    "images/thumbnails/slider_3.webp"
]

for img_path in images_to_darken:
    if os.path.exists(img_path):
        try:
            with Image.open(img_path) as img:
                # Enhance Brightness. A factor of 1.0 gives original image.
                # A factor of 0.0 gives a black solid image.
                enhancer = ImageEnhance.Brightness(img)
                darkened_img = enhancer.enhance(0.5) # 50% darker
                
                # Save it back overwriting the original
                darkened_img.save(img_path, "WEBP", quality=85)
                print(f"Successfully darkened {img_path}")
        except Exception as e:
            print(f"Failed to darken {img_path}: {e}")
    else:
        print(f"File not found: {img_path}")
