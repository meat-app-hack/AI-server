#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web application for nft price prediction
"""
from flask import Flask, request, Response
#from flask_cors import CORS
import jsonpickle
import time
import os
#os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

import predict

app = Flask(__name__)
port = os.environ.get('PORT', 2020)

#CORS(app)
    
@app.route('/predict', methods=['POST'])
def detect_recogn(): 
    """
    :input: vertical oriented nft image in base64 format
    :output: json dictionary with strings of nft predicted info
    """

    start_time = time.time()
    
    url_json = request.get_json(force=True)
    url = url_json['passbase64str']

    img_array = predict.url_to_array(url)
    
    class_number, class_probability = predict.predict_class(img_array)
    dollar_price = predict.predict_price(class_number, class_probability)
    time_spent = time.time() - start_time

    #print('class_number: {}, class_probability: {}'.format(class_number, class_probability))
    #print('dollar_price:', dollar_price)

    response = {
        'dollar_price':str(dollar_price), 
        'class_number':str(class_number),
        'class_probability':str(class_probability),
        'time_spent':str(time_spent)       
    }
    #print('response is ', response)
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype='application/json')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port, debug=False, threaded=True)