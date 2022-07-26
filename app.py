from flask import Flask
from flask_restful import Api
from pyfiglet import figlet_format

app = Flask(__name__)
api = Api(app)

from routes.asciiRoute import AsciiRoute


@app.route("/")
def home():
    return {"message":"This is initial route"}

@app.route("/ascii_pre")
def ascii_pre():
    fonts = request.args.get('fonts')
    query = request.args.get('query')
    art=figlet_format(text=query,font=fonts)
    return f"<pre>{art}</pre>"

api.add_resource(AsciiRoute, "/ascii")

if __name__=="__main__":
    app.run(debug=True, port="5000")