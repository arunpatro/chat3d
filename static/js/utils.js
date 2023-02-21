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

  // Create the blue ball geometry
  var geometry = new THREE.SphereGeometry(0.5, 32, 32);
  
  // Create the Phong material with blue color and shiny reflection
  var material = new THREE.MeshPhongMaterial({ color: 0x0000ff, shininess: 100 });
  
  // Create the blue ball mesh
  var ball = new THREE.Mesh(geometry, material);
  // Center the ball around the origin
  ball.position.set(0, 0, 0);
  
  scene.add(ball);
  function animate() {
    requestAnimationFrame(animate);
    ball.rotation.y += 0.01;
    renderer.render(scene, camera);
  }
  // Call the animation function
  animate();
  
}

