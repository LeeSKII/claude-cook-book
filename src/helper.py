import base64
from pathlib import Path
import mimetypes
def create_image_message(image_path):
    file_abs_path = Path(image_path).absolute()
    base64_string = base64.b64encode(file_abs_path.read_bytes()).decode('utf-8')
    mime_type,_ = mimetypes.guess_type(image_path)
    image_message_block = {
        'type':'image',
        'source':{
            'type':'base64',
            'data':base64_string,
            'media_type':mime_type
        }
    }
    return image_message_block