import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from io import BytesIO
from PIL import Image
import base64
import requests

mean_class_prices =  [355.9935, 791.0966666666667, 517.2822884000001, 3071.3111970975415, 
                                854.3843999999998, 2014.3958122222223]
current_model = load_model('./data/6_class_4_layer_100epoch.h5')
img_size = (300, 300)

def base64_to_array(im_b64):   
    im_bytes = base64.b64decode(im_b64)
    buf = BytesIO(im_bytes)

    img_pil = Image.open(buf)
    img_pil = img_pil.resize(img_size)

    keras_img_array = image.img_to_array(img_pil)
    return np.expand_dims(keras_img_array, axis=0)

def predict_class(img_array, model=current_model):
    x = model.predict(img_array)

    class_probability = np.max(x)
    class_number = np.where(x == class_probability)
    return class_number[1][0], class_probability

def predict_price(class_number, class_probability):
    return class_probability * mean_class_prices[class_number]

def url_to_array(url):
    response = requests.get(url)
    img_pil = Image.open(BytesIO(response.content)) 
    print(np.shape(img_pil))

    if np.shape(img_pil)[2] == 4:
        img_pil.load()
        background = Image.new("RGB", img_pil.size, (255, 255, 255))
        background.paste(img_pil, mask=img_pil.split()[3])
        img_pil = background

    img_pil = img_pil.resize(img_size) 
    keras_img_array = image.img_to_array(img_pil)
    assert np.shape(keras_img_array) == (300, 300, 3)
    return np.expand_dims(keras_img_array, axis=0)

def test():
    path = './imgs/2.jpg'
    url = 'https://firebasestorage.googleapis.com/v0/b/message-app-dfc81.appspot.com/o/images%2F1046769.png?alt=media&amp;token=ffa4286a-8ef4-43be-8599-42b5bb1b5f4f'

    via_base64 = False
    if via_base64:
        with open(path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        img_array = base64_to_array(encoded_string)
    else:
        img_array = url_to_array(url)

    class_number, class_probability = predict_class(img_array)
    predicted_price = predict_price(class_number, class_probability)
    return print('predicted_price:', predicted_price)

#test()