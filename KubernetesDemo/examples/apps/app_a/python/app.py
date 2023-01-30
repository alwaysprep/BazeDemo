from flask import Flask

from src.about import about
from src.home import home


app = Flask(__name__)

app.register_blueprint(home, url_prefix="/")
app.register_blueprint(about, url_prefix="/about")

if __name__ == "__main__":
    app.run("0.0.0.0", port=8888)
