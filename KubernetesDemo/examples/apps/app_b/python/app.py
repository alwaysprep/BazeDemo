from flask import Flask

from src.home import home


app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8889)
