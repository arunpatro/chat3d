document.addEventListener("DOMContentLoaded", function() {
    // Get references to DOM elements
    var textbox = document.getElementById("textbox");
    var renderButton = document.getElementById("render-button");
  
    // Add event listener to render button
    renderButton.addEventListener("click", function() {
      generate(textbox.value);
    });
  });