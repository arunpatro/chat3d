// Create a scene
var scene = new THREE.Scene();
// Create a camera
var camera = new THREE.PerspectiveCamera(75, window.innerWidth / window.innerHeight, 0.1, 1000);

// Create a renderer
var renderer = new THREE.WebGLRenderer({ canvas: document.querySelector("#canvas") });
renderer.setSize(500, 500);
// renderer.setSize(window.innerWidth, window.innerHeight);
