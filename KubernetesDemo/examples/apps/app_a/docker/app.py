import json

from flask import Flask

from src.about import about
from src.home import home


app = Flask(__name__)
app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(about, url_prefix="/about")

with open('examples/apps/app_a/app_a.conf.json') as config_file:
    conf = json.load(config_file)


@app.route("/")
def root():
    return f"Welcome to {conf.get('name')}"

if __name__ == "__main__":
    app.run("0.0.0.0", port=conf.get("port"))
