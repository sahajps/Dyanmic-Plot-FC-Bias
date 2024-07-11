import numpy as np
import io
import base64
from .returnplot import gen_plot # type: ignore

def get_plot_data(integer_input, start_date_input, end_date_input):
    """
    Generate a plot and return its base64-encoded PNG data.

    Returns:
        str: Base64-encoded PNG image data.
    """
    
    buf = io.BytesIO()
    plt1 = gen_plot(int(integer_input), start_date_input, end_date_input)
    plt1.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    return plot_data