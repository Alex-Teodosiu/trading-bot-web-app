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

    // Filter logic
    var tabs = document.querySelectorAll('#positionFilterTabs .nav-link');
    var rows = document.querySelectorAll('#positionsTableBody tr');

    tabs.forEach(tab => {
        tab.addEventListener('click', function(event) {
            event.preventDefault();
            var filter = this.getAttribute('data-filter');

            // Remove active class from all tabs
            tabs.forEach(t => t.classList.remove('active'));
            // Add active class to the clicked tab
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

    // Search functionality
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

    // Trigger search on enter key press
    searchInput.addEventListener('keypress', function(event) {
        if (event.key === 'Enter') {
            searchButton.click();
        }
    });


    // Get the elements
    var plpc = document.getElementById('plpc');
    var pl = document.getElementById('pl');

    // Function to add sign and color
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

    // Apply the function to the elements
    addSignAndColor(plpc);
    addSignAndColor(pl);
});
