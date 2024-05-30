document.addEventListener('DOMContentLoaded', function() {
    var positionCounts = document.getElementById('positionCounts');
    var longCount = Number(positionCounts.getAttribute('data-long'));
    var shortCount = Number(positionCounts.getAttribute('data-short'));

    console.log('Long Count:', longCount);
    console.log('Short Count:', shortCount);

    var ctx = document.getElementById('positionDistributionChart').getContext('2d');
    var positionDistributionChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Long', 'Short'],
            datasets: [{
                data: [longCount, shortCount],
                backgroundColor: ['#FFCE56', '#FF6384']
            }]
        },
    });

    var tabs = document.querySelectorAll('#positionFilterTabs .nav-link');
    var rows = document.querySelectorAll('#positionsTableBody tr');

    tabs.forEach(tab => {
        tab.addEventListener('click', function(event) {
            event.preventDefault();
            var filter = this.getAttribute('data-filter');

            tabs.forEach(t => t.classList.remove('active'));
            this.classList.add('active');

            rows.forEach(row => {
                if (filter === 'all') {
                    row.style.display = '';
                } else {
                    row.style.display = row.getAttribute('data-side') === filter ? '' : 'none';
                }
            });
        });
    });


    var searchButton = document.getElementById('searchButton');
    var searchInput = document.getElementById('searchInput');

    searchButton.addEventListener('click', function() {
        var searchTerm = searchInput.value.toLowerCase();

        rows.forEach(row => {
            var symbol = row.getAttribute('data-symbol').toLowerCase();
            if (symbol.includes(searchTerm)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
    });


    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            searchButton.click();
        }
    });

    var plpc = document.getElementById('plpc');
    var pl = document.getElementById('pl');

    function addSignAndColor(element) {
        var originalText = element.innerText;
        var value = parseFloat(originalText.replace('%', '').replace('$', ''));
        if (value > 0) {
            element.style.color = 'green';
            if (!originalText.startsWith('+')) {
                element.innerText = '+' + originalText;
            }
        } else if (value < 0) {
            element.style.color = 'red';
            if (!originalText.startsWith('-')) {
                element.innerText = '-' + originalText;
            }
        }
    }

    addSignAndColor(plpc);
    addSignAndColor(pl);
});
