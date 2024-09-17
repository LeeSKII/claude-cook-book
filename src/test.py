from pathlib import Path
import base64
from helper import create_image_message

# print(base64.b64encode(Path('./images/images.jpg').absolute().read_bytes()).decode('utf-8'))

print(create_image_message('./images/images.jpg')) 