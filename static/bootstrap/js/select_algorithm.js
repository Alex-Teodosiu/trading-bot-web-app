document.addEventListener('DOMContentLoaded', function () {
    var algorithmModal = new bootstrap.Modal(document.getElementById('algorithmModal'));
    var algorithmModalLabel = document.getElementById('algorithmModalLabel');
    var runAlgorithmButton = document.getElementById('runAlgorithmButton');
    var algorithmContainer = document.querySelector('.new-algorithm-container');
    var selectedAlgorithm = '';

    // Load running algorithms on page load
    fetch('/algorithm/load-running-algorithms', {
        method: 'GET',
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        console.log('Running algorithms:', data);

        data.running_algorithms.forEach(algorithm => {
            // Create a new card for each running algorithm
            var newCard = document.createElement('div');
            newCard.className = 'col-md-4 mb-4';
            newCard.innerHTML = `
                <div class="card h-100 shadow-sm border-0">
                    <div class="card-body d-flex flex-column">
                        <h4 class="card-title text-center">${algorithm.algorithm}</h4>
                        <p class="flex-grow-1">Symbol: ${algorithm.symbol}</p>
                        <p>Running since: ${algorithm.timestamp}</p>
                        <div class="d-grid gap-2 mt-auto">
                            <button class="btn btn-danger stop-algorithm-button" data-algorithm="${algorithm.algorithm}" data-symbol="${algorithm.symbol}">Stop Algorithm</button>
                        </div>
                    </div>
                </div>
            `;

            // Append the new card to the container
            algorithmContainer.appendChild(newCard);

            // Add event listener to the stop button
            var stopButton = newCard.querySelector('.stop-algorithm-button');
            stopButton.addEventListener('click', function () {
                stopAlgorithm(newCard, algorithm.algorithm, algorithm.symbol);
            });
        });
    })
    .catch((error) => {
        console.error('Error loading running algorithms:', error);
        alert('Failed to load running algorithms. Please try again later.');
    });

    document.getElementById('algorithmModal').addEventListener('show.bs.modal', function (event) {
        var button = event.relatedTarget;
        selectedAlgorithm = button.getAttribute('data-algorithm');
        algorithmModalLabel.textContent = 'Run ' + selectedAlgorithm + ' Algorithm';
    });

    runAlgorithmButton.addEventListener('click', function () {
        var symbol = document.getElementById('algorithmSymbol').value;

        // Check if the symbol input is empty
        if (!symbol) {
            alert('Please enter a symbol.');
            return;
        }

        // Prepare the request payload
        var payload = {
            user_id: 'd811a8c7-3b77-46d9-873f-e471b8f5935b',
            symbol: symbol,
            algorithm_name: selectedAlgorithm,
            time_stamp: new Date().toISOString().split('T')[0]
        };

        // Send the request to the backend
        fetch('/algorithm/save-algorithm-run', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Success:', data);

            // Create a new card for the running algorithm
            var newCard = document.createElement('div');
            newCard.className = 'col-md-4 mb-4';
            newCard.innerHTML = `
                <div class="card h-100 shadow-sm border-0">
                    <div class="card-body d-flex flex-column">
                        <h4 class="card-title text-center">${selectedAlgorithm}</h4>
                        <p class="flex-grow-1">Symbol: ${symbol}</p>
                        <p>Running since: ${new Date().toLocaleString()}</p>
                        <div class="d-grid gap-2 mt-auto">
                            <button class="btn btn-danger stop-algorithm-button" data-algorithm="${selectedAlgorithm}" data-symbol="${symbol}">Stop Algorithm</button>
                        </div>
                    </div>
                </div>
            `;

            // Append the new card to the container
            algorithmContainer.appendChild(newCard);

            // Close the modal after running the algorithm
            algorithmModal.hide();

            // Ensure modal backdrop is removed
            document.body.classList.remove('modal-open');
            document.querySelector('.modal-backdrop').remove();

            // Add event listener to the stop button
            var stopButton = newCard.querySelector('.stop-algorithm-button');
            stopButton.addEventListener('click', function () {
                stopAlgorithm(newCard, selectedAlgorithm, symbol);
            });
        })
        .catch((error) => {
            console.error('Error:', error);
            alert('Failed to run algorithm. Please try again later.');
        });
    });

    // Create new algorithm (placeholder functionality)
    document.getElementById('createNewAlgorithmButton').addEventListener('click', function () {
        alert('This functionality is coming soon!');
    });

    // Function to stop the algorithm
    function stopAlgorithm(cardElement, algorithmName, symbol) {
        // Prepare the request payload
        var payload = {
            user_id: 'd811a8c7-3b77-46d9-873f-e471b8f5935b',
            symbol: symbol,
            algorithm_name: algorithmName
        };

        // Send the request to the backend
        fetch('/algorithm/stop-algorithm', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        })
        .then(response => response.json())
        .then(data => {
            console.log('Algorithm stopped:', data);
            alert('Algorithm has been stopped.');
            // Remove the card from the DOM
            cardElement.remove();
        })
        .catch((error) => {
            console.error('Error stopping algorithm:', error);
            alert('Failed to stop the algorithm. Please try again later.');
        });
    }
});
