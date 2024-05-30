document.addEventListener('DOMContentLoaded', function() {
    console.log("DOM fully loaded and parsed");

    const ctx = document.getElementById('stockChart').getContext('2d');
    let stockChart = new Chart(ctx, {
        type: 'candlestick',
        data: {
            datasets: [{
                label: 'Candlestick Data',
                data: [],
                categoryPercentage: 0.05, 
                barPercentage: 0.5, 
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                title: {
                    display: true,
                    text: 'GOOGL'
                },
                legend: {
                    display: false
                }
            },
            scales: {
                x: {
                    type: 'time',
                    time: {
                        unit: 'day',
                        tooltipFormat: 'MMM dd, yyyy',
                        displayFormats: {
                            day: 'MMM d'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Date'
                    },
                    ticks: {
                        maxRotation: 0,
                        autoSkip: false,
                        stepSize: 1,
                        maxTicksLimit: 20
                    },
                    offset: true
                },
                y: {
                    title: {
                        display: true,
                        text: 'Price'
                    }
                }
            }
        }
    });

    const fetchData = async (symbol) => {
        console.log(`Fetching data for symbol: ${symbol}`);
        try {
            const response = await fetch(`/stock_historical_market_data?symbol=${symbol}&last_x_days=45`);
            const data = await response.json();
            console.log("Data fetched successfully:", data);

            if (!Array.isArray(data)) {
                throw new Error('Expected an array but received something else');
            }

            const today = new Date();
            const formattedData = data.map((item, index) => {
                const date = new Date();
                date.setDate(today.getDate() - (data.length - 1 - index));
                return {
                    x: date,
                    o: item.open,
                    h: item.high,
                    l: item.low,
                    c: item.close
                };
            });

            console.log("Formatted data for candlestick chart:", formattedData);

            stockChart.data.datasets[0].data = formattedData;
            stockChart.options.plugins.title.text = symbol;  
            stockChart.update();

            console.log("Chart updated successfully");
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    document.getElementById('searchButton').addEventListener('click', () => {
        const symbol = document.getElementById('symbolInput').value.toUpperCase();
        fetchData(symbol);
    });

    // Load default data
    fetchData('GOOGL'); 
});
