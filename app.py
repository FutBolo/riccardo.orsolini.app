import os
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')
app.secret_key = os.environ.get("SESSION_SECRET", "dev-secret-key-for-orsolini-site")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/storico')
def storico():
    return render_template('storico.html')

@app.route('/big-match.html')
def big_match():
    return render_template('big-match.html')

@app.route('/avversari-preferiti.html')
def avversari_preferiti():
    return render_template('avversari-preferiti.html')
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
