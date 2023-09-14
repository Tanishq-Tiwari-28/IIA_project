function showWarningMessage() {
    var inputElement = document.getElementById("input");
    var warningMessage = document.getElementById("warning-message");

    if (inputElement.value.trim() === "") {
        warningMessage.style.display = "block";
        return true; // Return true to indicate a warning
    } else {
        warningMessage.style.display = "none";
        return false; // Return false when no warning
    }
}

// ... Other code ...

// Inside your form submission logic
document.getElementById("submit-btn").addEventListener("click", function (event) {
    if (showWarningMessage()) {
        event.preventDefault(); // Prevent form submission when there's a warning
    }
})