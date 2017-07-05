from flask import Flask

app = Flask(__name__)

links = []


@app.route('/v1/links', methods=['GET'])
def list_links():
    return links, 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
