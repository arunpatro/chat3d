function generate() {
  // var prompt = document.getElementById('textbox').value;
  var prompt = "heelo"

  // Make a POST request to the Flask server to get the Three.js code
  fetch('/generate', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ prompt: prompt })
  })
    .then(response => response.json())
    .then(data => {
      // Create the Three.js objects from the generated code
      eval(data.code);
    })
    .catch(error => console.error(error));
}
