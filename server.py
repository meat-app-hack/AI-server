from flask import Flask, request, Response
from chatbot import ask, append_interaction_to_chat_log
import jsonpickle

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    dict = request.get_json(force=True)
    question = dict['Body']


    answer = ask(question)
    
    response = {
        'question':str(question), 
        'answer':str(answer)
       
    }
    print('response is ', response)
    response_pickled = jsonpickle.encode(response)

    return Response(response=response_pickled, status=200, mimetype='application/json')

if __name__ == '__main__':

    app.run(host='0.0.0.0', port=2020, debug=True, threaded=True)