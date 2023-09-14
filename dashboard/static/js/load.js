document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("contact-form");
    const loadingOverlay = document.getElementById("loading-overlay");

    form.addEventListener("submit", function() {
        // Show the loading animation
        form.style.display = 'none'
        loadingOverlay.style.display = 'block'
        
    });
});

