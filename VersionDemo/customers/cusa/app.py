import sys

import flask
import numpy

import src.libx as libx
import src.liby as liby

from src.core.web.app import create_app
from src.libx.web.home import home
from src.liby.web.about import about


app = create_app()

app.register_blueprint(home, url_prefix="/home")
app.register_blueprint(about, url_prefix="/about")


@app.route('/')
def print_hello():
    return {
        "libx": libx.__version__,
        "liby": liby.__version__,
        "flask": flask.__version__,
        "numpy": numpy.__version__,
        "python": sys.version
    }



if __name__ == "__main__":
    app.run(host="0.0.0.0", port="9999", debug=True)
