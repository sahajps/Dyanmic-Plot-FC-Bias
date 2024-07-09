import numpy as np
import io
import base64
from .returnplot import gen_plot # type: ignore

def get_plot_data():
    """
    Generate a plot and return its base64-encoded PNG data.

    Returns:
        str: Base64-encoded PNG image data.
    """
    
    buf = io.BytesIO()
    plt1 = gen_plot()
    plt1.savefig(buf, format='png')
    buf.seek(0)
    plot_data = base64.b64encode(buf.read()).decode('utf-8')
    return plot_data