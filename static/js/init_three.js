// Create a scene
var scene = new THREE.Scene();
// Create a camera
var camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);

// Create a renderer
var renderer = new THREE.WebGLRenderer({ canvas: document.querySelector("#canvas"),  alpha: true  });
// renderer.setSize(window.innerWidth, window.innerHeight);
renderer.setSize(canvas.clientWidth, canvas.clientHeight);

// Create axes helper
var axesHelper = new THREE.AxesHelper(5);

// Add axes helper to the scene
scene.add(axesHelper);