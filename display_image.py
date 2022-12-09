import numpy as np
from PIL import Image
import base64
import io

def show(file):

    filename = file.filename
    img = Image.open(file.stream)
    with io.BytesIO() as buf:
        img.save(buf, 'jpeg')
        image_bytes = buf.getvalue()
    encoded_string = base64.b64encode(image_bytes).decode()  

    return encoded_string