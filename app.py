import distilbert_model as model
from flask import Flask, request, jsonify
app = Flask(__name__)


@app.route('/')
def hello():
    return 'Server is working!'

@app.route('/get_sentiment', methods = ['post'])
def get_sentiment():
    tx = request.get_json(force=True)
    text = tx['Review']
    res = model.get_prediction(text)
    return jsonify(result = res)

if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_reloader=False)