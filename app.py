from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Лабораторна робота 3 успішно запущена!"

@app.route('/submit', methods=['POST'])
def submit_name():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({"error": "Будь ласка, представтеся 'name'"}), 400
    name = data['name']
    return jsonify({"message": f"Дякую, {name}, дані отримано!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
