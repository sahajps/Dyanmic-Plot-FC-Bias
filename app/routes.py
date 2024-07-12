from flask import Blueprint, render_template, redirect, url_for, flash
from flask_socketio import emit
from . import socketio
from .utils.plotter import get_plot_data

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/paper')
def paper():
    return render_template('paper.html')

@main.route('/about')
def about():
    return render_template('about.html')

@socketio.on('request_plot_data')
def handle_plot_request(json):
    order_input = json.get('order_input', 'Alphabatic')
    integer_input = json.get('integer_input', 5)
    start_date_input = json.get('start_date_input', '2023-12-31')
    end_date_input = json.get('end_date_input', '2018-01-01')
    data = get_plot_data(order_input, integer_input, start_date_input, end_date_input)
    emit('plot_data', data)
