import json

from flask import Flask

from src.home import home


app = Flask(__name__)
app.register_blueprint(home, url_prefix="/home")

with open('examples/apps/app_b/app_b.conf.json') as config_file:
    conf = json.load(config_file)


@app.route("/")
def root():
    return f"Welcome to {conf.get('name')}"

if __name__ == "__main__":
    app.run("0.0.0.0", port=conf.get("port"))
