from flask import Flask, request, jsonify, render_template
from langchain.llms import OpenAI
from langchain import PromptTemplate

app = Flask(__name__, template_folder="templates", static_folder="static")
model = OpenAI(
    temperature=0.7,
    openai_api_key="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",
)

three_js_template_string = """
I want you to generate the code for three.js to generate one or more 3d models. For this task, we have already set the scene and camera for you. You only need to generate the code for the 3d models. This is the code for the scene and camera:

var scene = new THREE.Scene();
var camera = new THREE.PerspectiveCamera(75, canvas.clientWidth / canvas.clientHeight, 0.1, 1000);
var renderer = new THREE.WebGLRenderer({{ canvas: document.querySelector("#canvas"),  alpha: true  }});
renderer.setSize(canvas.clientWidth, canvas.clientHeight);
var axesHelper = new THREE.AxesHelper(5);
scene.add(axesHelper);

Here's an example of how to use this, given the prompt "mickey mouse head created with spheres with phong material that rotates around the y axis":
The output is the following code:

// Create a Mickey Mouse head
var headGeometry = new THREE.SphereGeometry(1.5, 32, 32);
var headMaterial = new THREE.MeshPhongMaterial({{ color: 0xffc1c1, shininess: 100 }});
var head = new THREE.Mesh(headGeometry, headMaterial);

// Create the ears
var earGeometry = new THREE.SphereGeometry(0.5, 16, 16);
var earMaterial = new THREE.MeshPhongMaterial({{ color: 0x000000, shininess: 100 }});
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

// Create an animation function
function animate() {{
  requestAnimationFrame(animate);
  mickeyGroup.rotation.y += 0.01;
  renderer.render(scene, camera);
}}

// Call the animation function
animate();

You should use this given prompt and generate the suitable code for three js: "{prompt}". 

Return the code as a string without any docstrings or english text, which will directly executed on the js console.
"""

prompt_template = PromptTemplate(
    input_variables=["prompt"],
    template=three_js_template_string,
)

# Index page (now using the index.html file)
@app.route("/")
def index():
    return render_template("index.html")


from sample_objects import mickey_mouse, ball

# print(mickey_mouse)


@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json["prompt"]
    print("Generating code for prompt: ", prompt)
    code = ball
    # code = model(prompt_template.format(prompt=prompt))

    # print(code)
    response = {"code": code}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
