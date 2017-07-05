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


@app.route('/v1/links/<int:link_id>', methods=['DELETE'])
def delete_link(link_id):
    global links

    for link in links:
        if link['id'] == link_id:
            delete_link = link
            break

    links.remove(delete_link)
    return '', 204


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
