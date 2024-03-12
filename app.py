

from flask import Flask, request, make_response, jsonify, json

from test import boo

app = Flask(__name__)


message_history = []

bot_history = []

cookie = []

@app.route('/xd')
def chat():
    response = make_response(app.send_static_file('xd.html'))
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    return response

@app.route('/api/send_message', methods=['POST'])
def send_message():
    data = request.get_json()
    message = data['message']
    

    user_cookie = request.cookies.get('user_id')
    
    cookie.append(user_cookie)
    
    

    response = boo(message)

    


    bot_history.append({"author": "Bot", "message": response})
    message_history.append({"author": "Вы", "message": message})
    
    # JSON
    return jsonify({"response": response})

@app.route('/api/get_message_history', methods=['GET'])
def get_message_history():
    full_history = message_history + bot_history
    return jsonify({"message_history": full_history})

if __name__ == '__main__':
    app.run(debug=True)



print(cookie)