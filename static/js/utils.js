function generate(prompt) {
  // Show the loading gif
  document.getElementById("loading").style.display = "block";

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
      // Hide the loading gif
      document.getElementById("loading").style.display = "none";

      // Create the Three.js objects from the generated code
      console.log(data.code)
      init_scene();
      console.log(scene);
      eval(data.code);
      document.getElementById("code").innerHTML = data.code;
    })
    .catch(error => console.error(error));
}

function init_scene() {
  // Create a scene
  var scene = new THREE.Scene();
  // Create a camera
  var camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);

  // Create a renderer
  var renderer = new THREE.WebGLRenderer({ canvas: document.querySelector("#canvas"), alpha: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);
  // renderer.setSize(window.innerWidth, window.innerHeight);

  // Create axes helper
  var axesHelper = new THREE.AxesHelper(5);
  scene.add(axesHelper);

  // Create a directional light
  var light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(0, 1, 1).normalize();
  scene.add(light);
}