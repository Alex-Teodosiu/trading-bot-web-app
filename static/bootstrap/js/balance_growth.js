document.addEventListener('DOMContentLoaded', function() {
    var balanceGrowthDataElement = document.getElementById('balanceGrowthData');
    var timestamps = balanceGrowthDataElement.getAttribute('data-timestamp').split(',').map(Number);
    var equity = balanceGrowthDataElement.getAttribute('data-equity').split(',').map(Number);

    console.log('Timestamps:', timestamps);
    console.log('Equity:', equity);

    var labels = timestamps.map(ts => new Date(ts * 1000));
    console.log('Labels:', labels);  // Debugging statement

    var ctx = document.getElementById('balanceGrowthChart').getContext('2d');
    var balanceGrowthChart = new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [{
                label: 'Equity',
                data: equity,
                borderColor: '#4caf50',
                fill: false
            }]
        },
        options: {
            responsive: true,
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day',
                        tooltipFormat: 'P'
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    }
                },
                y: {
                    beginAtZero: false,
                    title: {
                        display: true,
                        text: 'Equity'
                    }
                }
            }
        }
    });
});
