var camera, scene, renderer, geometry, material, mesh;

// init()
// animate()

function init() {
  // set the renderer
  renderer = new THREE.WebGLRenderer({ canvas: document.querySelector("#canvas"), alpha: true });
  renderer.setSize(canvas.clientWidth, canvas.clientHeight);

  // set the scene and the camera
  scene = new THREE.Scene();
  camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 1, 10000);
  camera.position.z = 5;
  scene.add(camera);

  // set the lights
  light = new THREE.DirectionalLight(0xffffff, 1);
  light.position.set(0, 1, 1).normalize();
  scene.add(light);


  // optionally add any objects to be present inititally
  // geometry = new THREE.SphereGeometry(2, 32, 32);
  // material = new THREE.MeshPhongMaterial();
  // geometry = new THREE.BoxGeometry(2, 2, 5);
  // material = new THREE.MeshNormalMaterial();
  // mesh = new THREE.Mesh(geometry, material);
  // scene.add(mesh)


}

function animate() {
  // by default rotate all objects
  requestAnimationFrame(animate);
  rotate_objs();
  renderer.render(scene, camera);
}

function rotate_objs() {
  scene.traverse(function (object) {
    if (object.type === 'Mesh') {
      object.rotation.x += 0.01;
      object.rotation.y += 0.02;
    }
  });
  // camera.rotation.z += 0.01
}

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
      var codebox = document.getElementById("code")
      codebox.textContent = data.code;
      Prism.highlightElement(codebox);
      init();
      eval(data.code);
      animate();
    })
    .catch(error => console.error(error));
}

document.addEventListener("DOMContentLoaded", function () {
  // Get references to DOM elements
  var textbox = document.getElementById("textbox");
  var renderButton = document.getElementById("render-button");

  // Add event listener to render button
  renderButton.addEventListener("click", function () {
    generate(textbox.value);
  });
});

// init_scene();