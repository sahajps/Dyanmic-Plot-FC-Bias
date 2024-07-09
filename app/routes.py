from flask import Blueprint, render_template
from flask_socketio import emit
from . import socketio
from .utils.plotter import get_plot_data
#from .utils.returnplot import gen_plot

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@socketio.on('request_plot_data')
def handle_plot_request(json):
    data = get_plot_data()
    emit('plot_data', data)
