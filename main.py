from flask import Flask, request, jsonify, render_template
from langchain.llms import OpenAI
from langchain import PromptTemplate, FewShotPromptTemplate
from sample_objects import examples, mickey_mouse, a_small_blue_ball
import pickle

app = Flask(__name__, template_folder="templates", static_folder="static")
model = OpenAI(
  temperature=0.5,
  openai_api_key="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",
)

template = """
Description: {description}
Code: {code}\n
"""

prefix = """I want you to generate the code for three.js to generate one or more 3d models. We need code for four things: 1. Objects 2. Camera 3. Scene 4. Lights. 
Given a description of the object, your task is to generate the code for the object and if neccessary group the objects to create a composite group object.
Return the code as a string without any docstrings or english text, which will directly executed on the js console. Ensure that the objects are not too small or big and must be visible from a camera with parameters:
camera = new THREE.PerspectiveCamera(50, canvas.clientWidth / canvas.clientHeight, 1, 10000);
camera.position.z = 500;
Here are a few examples of how to do this:"""

suffix = "Description: {description}\nCode:"

example_prompt = PromptTemplate(
  input_variables=["description", "code"],
  template=template,
)

# print(example_prompt.format(description="a asf b", code="se {x} asdf \n ome"))
prompt_builder = FewShotPromptTemplate(
  examples=examples,
  example_prompt=example_prompt,
  prefix=prefix,
  suffix="Description: {input}\nCode:",
  input_variables=["input"],
  example_separator="\n\n",
)

test_code = """
geometry = new THREE.SphereGeometry(100, 32, 32);
//material = new THREE.MeshBasicMaterial({ color: 0x0000ff });
material = new THREE.MeshPhongMaterial({ color: 0x0000ff, shininess: 100 });
ball = new THREE.Mesh(geometry, material);
scene.add(ball);
"""


# Index page (now using the index.html file)
@app.route("/")
def index():
  return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
  prompt = request.json["prompt"]
  print("Generating code for prompt: ", prompt)
  # code = test_code
  code = model(prompt_builder.format(input=prompt))
  print(code)
  with open(f"prompts_cache/prompt_{prompt}.pickle", "wb") as f:
    pickle.dump([prompt, code], f)

  response = {"code": code}
  return jsonify(response)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
