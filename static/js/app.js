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


function init_4canvases() {
  let canvases = document.querySelectorAll("#canvases canvas");

  // create a mesh for each canvas
  let meshes = [
    new THREE.Mesh(new THREE.SphereGeometry(2, 32, 32), new THREE.MeshPhongMaterial({ color: getRandomColor() })),
    new THREE.Mesh(new THREE.BoxGeometry(2, 2, 2), new THREE.MeshPhongMaterial({ color: 0xffff00, shininess: 100 })),
    new THREE.Mesh(new THREE.TorusGeometry(2, 1, 16, 32), new THREE.MeshNormalMaterial({ color: 0xff00ff })),
    new THREE.Mesh(new THREE.CylinderGeometry(0.3, 0.3, 5, 32), new THREE.MeshNormalMaterial())
  ];
  meshes[3].rotation.z = Math.PI / 2;

  // create a renderer and camera for each canvas
  for (let i = 0; i < canvases.length; i++) {
    let canvas = canvases[i];
    canvas.width = canvas.clientWidth;
    canvas.height = canvas.clientHeight;

    let scene = new THREE.Scene();
    let camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 1, 10000);
    camera.position.z = 5;
    let light = new THREE.DirectionalLight(0xffffff, 1);
    light.position.set(0, 1, 1).normalize();
    scene.add(light);

    let mesh = meshes[i];
    scene.add(mesh);

    let renderer = new THREE.WebGLRenderer({ canvas: canvas, alpha: true });
    renderer.setSize(canvas.clientWidth, canvas.clientHeight);

    let animate = function () {
      requestAnimationFrame(animate);
      mesh.rotation.x += 0.01;
      mesh.rotation.y += 0.02;
      renderer.render(scene, camera);
    }
    animate();
  }
}


function getRandomColor() {
  return '#' + Math.floor(Math.random() * 0xffffff).toString(16).padEnd(6, '0');
}


init_4canvases()