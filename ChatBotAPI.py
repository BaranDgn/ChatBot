from flask import Flask, request, jsonify
from main import chatWithB

app = Flask(__name__)


@app.route("/chat", methods=['POST'])
def chatBot():
    chatInput = request.form['chatInput']
    chatReply = chatWithB(chatInput)
    return jsonify(chatBotReply=chatReply)


if __name__ == '__main__':
    app.run(host='192.168.1.3', port=5000, debug=True)
