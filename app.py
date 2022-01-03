from flask import Flask
from automobiles import automobiles_bp

app = Flask(__name__)
app.register_blueprint(automobiles_bp, url_prefix='/automobiles')



@app.route('/')
def home():
    return { 'message': 'this is the homepage' }


if __name__ == '__main__':
    app.run(debug=True)
