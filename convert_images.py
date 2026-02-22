import os
import subprocess
import sys

try:
    from PIL import Image
    import pillow_heif
    pillow_heif.register_heif_opener()
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pillow-heif", "pillow"])
    from PIL import Image
    import pillow_heif
    pillow_heif.register_heif_opener()

dir_path = r"C:\Users\TestSolutions\Documents\La-Jiraffa\images\onSite\getQuotation"
for fn in os.listdir(dir_path):
    ext = fn.lower().split('.')[-1]
    if ext in ['heic', 'png', 'jpg', 'jpeg']:
        try:
            img = Image.open(os.path.join(dir_path, fn))
            out_name = os.path.splitext(fn)[0] + '.webp'
            img.save(os.path.join(dir_path, out_name), 'WEBP', quality=85)
            print(f"Converted {fn} to {out_name}")
        except Exception as e:
            print(f"Failed to convert {fn}: {e}")
