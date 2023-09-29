from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def health_check():
    # modify this to try a connection to all dependencies and return healthy or a specific outage issue
    return jsonify(status='healthy')

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=60010)
