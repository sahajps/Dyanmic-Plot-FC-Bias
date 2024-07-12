document.addEventListener('DOMContentLoaded', (event) => {
    var socket = io();

    function requestPlotUpdate() {
        let orderInput = document.getElementById('order-input').value;
        let integerInput = document.getElementById('integer-input').value;
        let startDateInput = document.getElementById('start-date-input').value;
        let endDateInput = document.getElementById('end-date-input').value;

        let dateObject1 = new Date(startDateInput);
        let dateObject2 = new Date(endDateInput);
        
        if (dateObject1 > dateObject2) {
            $('#error-message').text('Resetting date range to default as start date must be less than end date.').show();
            $('#start-date-input').val('2018-01-01');
            $('#end-date-input').val('2023-12-31');
            startDateInput = document.getElementById('start-date-input').value;
            endDateInput = document.getElementById('end-date-input').value;
        } else {
            $('#error-message').hide();
        }

        console.log(endDateInput)
        socket.emit('request_plot_data', {
            order_input: orderInput,
            integer_input: integerInput,
            start_date_input: startDateInput,
            end_date_input: endDateInput
        });
    }

    // Initial plot update
    requestPlotUpdate();

    document.getElementById('order-input').addEventListener('change', requestPlotUpdate);
    document.getElementById('integer-input').addEventListener('change', requestPlotUpdate);
    document.getElementById('start-date-input').addEventListener('change', requestPlotUpdate);
    document.getElementById('end-date-input').addEventListener('change', requestPlotUpdate);

    socket.on('plot_data', function(data) {
        document.getElementById('plot').src = 'data:image/png;base64,' + data;
    });
});
