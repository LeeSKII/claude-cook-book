from pathlib import Path
import base64

print(base64.b64encode(Path('./images/images.jpg').absolute().read_bytes()).decode('utf-8'))