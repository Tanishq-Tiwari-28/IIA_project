document.addEventListener("DOMContentLoaded", function () {
    const errorBox = document.getElementById("errorBox");
  
    // Slide in the error box with animation
    function slideInErrorBox() {
      errorBox.style.display = "block";
      setTimeout(function () {
        errorBox.classList.add("show");
      }, 10); // Small delay for smoother animation
      setTimeout(hideErrorBox, 7000); // Hide after 5 seconds (adjust as needed)
    }
  
    // Hide the error box
    function hideErrorBox() {
      errorBox.classList.remove("show");
      setTimeout(function () {
        errorBox.style.display = "none";
      }, 300); // Hide animation duration
    }
  
    // Call the function to show the error box
    slideInErrorBox();
  });
  