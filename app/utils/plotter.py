import numpy as np
import io
import base64
from datetime import datetime
from .returnplot import gen_plot # type: ignore

def get_plot_data(order, integer_input, start_date_input, end_date_input):
    """
    Generate a plot and return its base64-encoded PNG data.

    Args:
        order (str): The order in which to sort the entities' data for plotting.
        integer_input (str): An integer value in string format to be used in the plot generation.
        start_date_input (str): The start date for the data range to be plotted, in the format 'YYYY-MM-DD'.
        end_date_input (str): The end date for the data range to be plotted, in the format 'YYYY-MM-DD'.

    Returns:
        str: Base64-encoded PNG image data representing the generated plot.
    """
    
    buf = io.BytesIO()
    integer_input = int(integer_input)
    start_date_input = datetime.strptime(start_date_input, '%Y-%m-%d')
    end_date_input = datetime.strptime(end_date_input, '%Y-%m-%d')
    plt1 = gen_plot(order, integer_input, start_date_input, end_date_input)
    plt1.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    return plot_data