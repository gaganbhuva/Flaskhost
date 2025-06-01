from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>Hello World! My Flask App on Render!</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1><p>This Flask app is permanently hosted!</p>'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)