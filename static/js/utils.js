function generate(prompt) {

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
      console.log(data.code)
      eval(data.code);
      document.getElementById("code").innerHTML = data.code;
    })
    .catch(error => console.error(error));
}


