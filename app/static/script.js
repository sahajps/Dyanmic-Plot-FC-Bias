document.addEventListener('DOMContentLoaded', (event) => {
    var socket = io();

    function requestPlotUpdate() {
        const integerInput = document.getElementById('integer-input').value;
        const startDateInput = document.getElementById('start-date-input').value;
        const endDateInput = document.getElementById('end-date-input').value;

        socket.emit('request_plot_data', {
            integer_input: integerInput,
            start_date_input: startDateInput,
            end_date_input: endDateInput
        });
    }

    // Initial plot update
    requestPlotUpdate();

    document.getElementById('integer-input').addEventListener('change', requestPlotUpdate);
    document.getElementById('start-date-input').addEventListener('change', requestPlotUpdate);
    document.getElementById('end-date-input').addEventListener('change', requestPlotUpdate);

    socket.on('plot_data', function(data) {
        document.getElementById('plot').src = 'data:image/png;base64,' + data;
    });
});
