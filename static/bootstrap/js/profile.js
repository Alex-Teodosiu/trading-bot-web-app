document.addEventListener('DOMContentLoaded', function() {
    console.log("Document is ready");

    var updateProfileButton = document.getElementById('updateProfileButton');
    var deleteAccountButton = document.getElementById('deleteAccountButton');
    var confirmDeleteButton = document.getElementById('confirmDeleteButton');
    var confirmationModal = new bootstrap.Modal(document.getElementById('confirmationModal'));

    updateProfileButton.addEventListener('click', function() {
        console.log("Update Profile Button Clicked");
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        console.log("Email value retrieved:", email);
        console.log("Password value retrieved:", password);

        if (!email || !password) {
            console.error("Email or Password is missing");
            alert("Email and Password cannot be empty.");
            return;
        }

        console.log("Making fetch request to /profile/update");
        fetch('/profile/update', {
            method: 'PUT',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email, password: password })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Update Success:", data);
            alert('Password updated successfully.');
        })
        .catch((error) => {
            console.error("Update Error:", error);
            alert('An error occurred: ' + error.message);
        });
    });

    deleteAccountButton.addEventListener('click', function() {
        console.log("Delete Account Button Clicked");
        confirmationModal.show();
    });

    confirmDeleteButton.addEventListener('click', function() {
        console.log("Confirm Delete Button Clicked");
        const email = document.getElementById('email').value;
        const password = document.getElementById('password').value;
        console.log("Email value retrieved:", email);
        console.log("Password value retrieved:", password);

        if (!email) {
            console.error("Email is missing");
            alert("Email and Password cannot be empty.");
            return;
        }

        console.log("Making fetch request to /profile/delete");
        fetch('/profile/delete', {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: email, password: password })
        })
        .then(response => response.json())
        .then(data => {
            console.log("Delete Success:", data);
            alert('User deleted successfully.');
            window.location.href = '/';
        })
        .catch((error) => {
            console.error("Delete Error:", error);
            alert('An error occurred: ' + error.message);
        });
    });
});
