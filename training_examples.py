EXAMPLES = [{
  "description":
  "a blue ball with phong reflection",
  "code":
  """
geometry = new THREE.SphereGeometry(2, 32, 32);
material = new THREE.MeshPhongMaterial({{ color: 0x0000ff, shininess: 100 }});
ball = new THREE.Mesh(geometry, material);
scene.add(ball);
"""
}, {
  "description":
  "a green cube with phong reflection",
  "code":
  """
geometry = new THREE.BoxGeometry(2, 2, 2);
material = new THREE.MeshPhongMaterial({{ color: 0x00ff00, shininess: 100 }});
ball = new THREE.Mesh(geometry, material);
scene.add(ball);
"""
}, {
  "description":
  "two green balls side by side, one with matte finish and the other with phong reflection",
  "code":
  """
matteGeometry = new THREE.SphereGeometry(1, 32, 32);
matteMaterial = new THREE.MeshLambertMaterial({{ color: 0x00ff00 }});
matteBall = new THREE.Mesh(matteGeometry, matteMaterial);
matteBall.position.x = -1.5;

shinyGeometry = new THREE.SphereGeometry(1, 32, 32);
shinyMaterial = new THREE.MeshPhongMaterial({{ color: 0x00ff00, shininess: 100 }});
shinyBall = new THREE.Mesh(shinyGeometry, shinyMaterial);
shinyBall.position.x = 1.5;

scene.add(matteBall);
scene.add(shinyBall);
"""
}, {
  "description":
  "two green balls cylinders",
  "code":
  """
var cylinderGeometry1 = new THREE.CylinderGeometry(1, 1, 2, 32);
var cylinderMaterial1 = new THREE.MeshLambertMaterial({{ color: 0x00ff00 }});
var cylinder1 = new THREE.Mesh(cylinderGeometry1, cylinderMaterial1);
cylinder1.position.x = -1.5;

var cylinderGeometry2 = new THREE.CylinderGeometry(1, 1, 2, 32);
var cylinderMaterial2 = new THREE.MeshLambertMaterial({{ color: 0x00ff00 }});
var cylinder2 = new THREE.Mesh(cylinderGeometry2, cylinderMaterial2);
cylinder2.position.x = 1.5;

scene.add(cylinder1);
scene.add(cylinder2);
"""
}, {
  "description":
    "three cubes",
    "code":
"""
var cubeGeometry1 = new THREE.BoxGeometry(2, 2, 2);
var cubeMaterial1 = new THREE.MeshLambertMaterial({{ color: 0xff0000 }});
var cube1 = new THREE.Mesh(cubeGeometry1, cubeMaterial1);
cube1.position.x = -2;

var cubeGeometry2 = new THREE.BoxGeometry(2, 2, 2);
var cubeMaterial2 = new THREE.MeshLambertMaterial({{ color: 0x00ff00 }});
var cube2 = new THREE.Mesh(cubeGeometry2, cubeMaterial2);
cube2.position.x = 0;

var cubeGeometry3 = new THREE.BoxGeometry(2, 2, 2);
var cubeMaterial3 = new THREE.MeshLambertMaterial({{ color: 0x0000ff }});
var cube3 = new THREE.Mesh(cubeGeometry3, cubeMaterial3);
cube3.position.x = 2;

scene.add(cube1);
scene.add(cube2);
scene.add(cube3);
"""
}]



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


table = """
// Create the table top
var tableTopGeometry = new THREE.BoxGeometry(2, 0.1, 1);
var tableTopMaterial = new THREE.MeshPhongMaterial({ color: 0x886633, shininess: 100 });
var tableTop = new THREE.Mesh(tableTopGeometry, tableTopMaterial);
tableTop.position.set(0, 0.55, 0);

// Create the table legs
var tableLegGeometry = new THREE.BoxGeometry(0.1, 0.4, 0.1);
var tableLegMaterial = new THREE.MeshPhongMaterial({ color: 0x886633, shininess: 100 });
var tableLeg1 = new THREE.Mesh(tableLegGeometry, tableLegMaterial);
tableLeg1.position.set(-0.9, 0.2, -0.4);
var tableLeg2 = new THREE.Mesh(tableLegGeometry, tableLegMaterial);
tableLeg2.position.set(-0.9, 0.2, 0.4);
var tableLeg3 = new THREE.Mesh(tableLegGeometry, tableLegMaterial);
tableLeg3.position.set(0.9, 0.2, -0.4);
var tableLeg4 = new THREE.Mesh(tableLegGeometry, tableLegMaterial);
tableLeg4.position.set(0.9, 0.2, 0.4);

// Add the table top and legs to a group
var tableGroup = new THREE.Group();
tableGroup.add(tableTop);
tableGroup.add(tableLeg1);
tableGroup.add(tableLeg2);
tableGroup.add(tableLeg3);
tableGroup.add(tableLeg4);

// Add the table group to the scene
scene.add(tableGroup);

// Create a directional light
var light = new THREE.DirectionalLight(0xffffff, 1);
light.position.set(0, 1, 1).normalize();
scene.add(light);

// Position the camera
camera.position.set(0, 1, 3);

// Create an animation function
function animate() {
  requestAnimationFrame(animate);
  tableGroup.rotation.y += 0.01;
  renderer.render(scene, camera);
}

// Call the animation function
animate();

"""

a_small_blue_ball = """
geometry = new THREE.SphereGeometry(100, 32, 32);
material = new THREE.MeshPhongMaterial({ color: 0x0000ff, shininess: 100 });
ball = new THREE.Mesh(geometry, material);
scene.add(ball);
"""
