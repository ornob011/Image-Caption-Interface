from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.applications import DenseNet201
import numpy as np
import pickle5 as pickle
from tensorflow.keras.models import Model
from PIL import Image
from PIL.Image import Image as PILImage
import io
from typing import Union

cnn_model = DenseNet201(weights='imagenet')
caption_model = load_model('model.h5')


def idx_to_word(integer,tokenizer):
    
    for word, index in tokenizer.word_index.items():
        if index==integer:
            return word
    return None


def predict_caption(data: Union[bytes, PILImage, np.ndarray], max_length = 34)-> Union[bytes, PILImage, np.ndarray]:
    
    if isinstance(data, PILImage):
        img = data
    elif isinstance(data, bytes):
        img = Image.open(io.BytesIO(data))
    elif isinstance(data, np.ndarray):
        img = Image.fromarray(data)
    else:
        raise ValueError("Input type {} is not supported.".format(type(data)))
        
    
    
    fe = Model(inputs=cnn_model.input, outputs=cnn_model.layers[-2].output)
    
    with open('tokenizer.pickle', 'rb') as handle:
        tokenizer = pickle.load(handle)

    newsize = (224, 224)
    img = img.resize(newsize)
    img = img_to_array(img) 
    img = img/255.

    img = np.expand_dims(img,axis=0)
    feature = fe.predict(img, verbose=0)
        
    in_text = "startseq"
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], max_length)

        y_pred = caption_model.predict([feature,sequence])
        y_pred = np.argmax(y_pred)
        
        word = idx_to_word(y_pred, tokenizer)
        
        if word is None:
            break
            
        in_text+= " " + word
        
        if word == 'endseq':
            break
    in_text = in_text.replace('startseq', '')
    in_text = in_text.replace('endseq', '')  
    return in_text
