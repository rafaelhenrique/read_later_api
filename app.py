from flask import Flask, jsonify

app = Flask(__name__)

links = []


@app.route('/v1/links', methods=['GET'])
def list_links():
    return jsonify(links), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
