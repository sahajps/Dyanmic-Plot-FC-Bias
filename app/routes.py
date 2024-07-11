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
    integer_input = json.get('integer_input', 5)
    start_date_input = json.get('start_date_input', '2024-01-01')
    end_date_input = json.get('end_date_input', '2024-01-01')
    data = get_plot_data(integer_input, start_date_input, end_date_input)
    emit('plot_data', data)
