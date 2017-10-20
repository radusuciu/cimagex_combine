from flask import Blueprint, send_file, render_template, request
import cimagex_combine.api as api


home = Blueprint('home', __name__,
                 template_folder='templates',
                 static_folder='static')


@home.route('/')
def index():
    bootstrap = None
    return render_template('index.html', bootstrap=bootstrap)
