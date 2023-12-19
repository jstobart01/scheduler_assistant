from flask import Flask, render_template
from waitress import serve

# Jackson's Calculator
# Menu Page

app = Flask(__name__)

# Calling the main page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# For local hosting
if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8000)