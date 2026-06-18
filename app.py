from flask import Flask, send_file

app = Flask(__name__)

@app.route('/')
def serve_index():
    # Serves the index.html file located in the src directory
    return send_file('src/index.html')

if __name__ == '__main__':
    # debug=True automatically reloads the server when you make changes
    app.run(host="0.0.0.0", debug=True, port=80)
