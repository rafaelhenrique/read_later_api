from flask import Flask, jsonify, request

app = Flask(__name__)

links = []
index = 0


@app.route('/v1/links', methods=['GET'])
def list_links():
    return jsonify(links), 200


@app.route('/v1/links', methods=['POST'])
def insert_links():
    global index
    global links

    link = request.json['link']
    description = request.json['description']
    index += 1
    data = {
        'id': index,
        'link': link,
        'description': description,
    }
    links.append(data)
    return jsonify(data), 201


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
