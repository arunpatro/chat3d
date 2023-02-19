mickey_mouse = """
// Create a Mickey Mouse head
var headGeometry = new THREE.SphereGeometry(1.5, 32, 32);
var headMaterial = new THREE.MeshPhongMaterial({ color: 0xffc1c1, shininess: 100 });
var head = new THREE.Mesh(headGeometry, headMaterial);
// Create the ears
var earGeometry = new THREE.SphereGeometry(0.5, 16, 16);
var earMaterial = new THREE.MeshPhongMaterial({ color: 0x000000, shininess: 100 });
var leftEar = new THREE.Mesh(earGeometry, earMaterial);
leftEar.position.set(1, 1.5, 0.5);
var rightEar = new THREE.Mesh(earGeometry, earMaterial);
rightEar.position.set(-1, 1.5, 0.5);
// Create a group and add the head and ears to it
var mickeyGroup = new THREE.Group();
mickeyGroup.add(head);
mickeyGroup.add(leftEar);
mickeyGroup.add(rightEar);
// Add the group to the scene
scene.add(mickeyGroup);
// Create a directional light
var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 1, 1).normalize();
scene.add(light);
// Create axes helper
var axesHelper = new THREE.AxesHelper(5);
// axesHelper.material.setColors(THREE.Color(0xff0000), THREE.Color(0x00ff00), THREE.Color(0x0000ff));
// Add axes helper to the scene
scene.add(axesHelper);
// Position the camera
camera.position.z = 5;
// Create an animation function
function animate() {
  requestAnimationFrame(animate);
  mickeyGroup.rotation.y += 0.01;
  renderer.render(scene, camera);
}
// Call the animation function
animate();
"""


ball = """
// Create a pink ping ball
var ballRadius = 1;
var ballGeometry = new THREE.SphereGeometry(ballRadius, 32, 32);
var ballMaterial = new THREE.MeshBasicMaterial({ color: 0xff69b4 });
var ball = new THREE.Mesh(ballGeometry, ballMaterial);

// Center the ball around the origin
ball.position.set(0, 0, 0);

// Add the ping ball to the scene
scene.add(ball);

// Create a directional light
var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 1, 1).normalize();
scene.add(light);

// Create axes helper
var axesHelper = new THREE.AxesHelper(5);
// axesHelper.material.setColors(THREE.Color(0xff0000), THREE.Color(0x00ff00), THREE.Color(0x0000ff));
// Add axes helper to the scene
scene.add(axesHelper);
// Position the camera
camera.position.z = 5;
// Create an animation function
function animate() {
  requestAnimationFrame(animate);
  ball.rotation.y += 0.01;
  renderer.render(scene, camera);
}
// Call the animation function
animate();
"""