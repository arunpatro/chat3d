from flask import Flask, request, jsonify, render_template
from langchain.llms import OpenAI
from langchain import PromptTemplate, FewShotPromptTemplate
from training_examples import EXAMPLES
# from langchain.prompts.example_selector.ngram_overlap import NGramOverlapExampleSelector
from langchain.prompts.example_selector import LengthBasedExampleSelector
import pickle
from datetime import datetime

app = Flask(__name__, template_folder="templates", static_folder="static")
model = OpenAI(
  temperature=0.4,
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
camera.position.z = 5;
Here are a few examples of how to do this:"""

suffix = "Description: {description}\nCode:"

example_prompt = PromptTemplate(
  input_variables=["description", "code"],
  template=template,
)

# prompt_builder = FewShotPromptTemplate(
#   examples=examples,
#   example_prompt=example_prompt,
#   prefix=prefix,
#   suffix="Description: {input}\nCode:",
#   input_variables=["input"],
#   example_separator="\n\n",
# )

example_selector = LengthBasedExampleSelector(
    # These are the examples it has available to choose from.
    examples=EXAMPLES, 
    # This is the PromptTemplate being used to format the examples.
    example_prompt=example_prompt, 
    # This is the maximum length that the formatted examples should be.
    # Length is measured by the get_text_length function below.
    max_length=25,
    # This is the function used to get the length of a string, which is used
    # to determine which examples to include. It is commented out because
    # it is provided as a default value if none is specified.
    # get_text_length: Callable[[str], int] = lambda x: len(re.split("\n| ", x))
)

# example_selector = NGramOverlapExampleSelector(
#     examples=EXAMPLES, 
#     example_prompt=example_prompt, 
#     # This is the threshold, at which selector stops.
#     # It is set to -1.0 by default.
#     threshold=-1.0,
#     # For negative threshold:
#     # Selector sorts examples by ngram overlap score, and excludes none.
#     # For threshold greater than 1.0:
#     # Selector excludes all examples, and returns an empty list.
#     # For threshold equal to 0.0:
#     # Selector sorts examples by ngram overlap score,
#     # and excludes those with no ngram overlap with input.
# )

prompt_builder = FewShotPromptTemplate(
  examples=EXAMPLES,
  # example_selector=example_selector,
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
  with open(
      f"prompts_cache/prompt_{prompt}_{datetime.now().isoformat()}.pickle",
      "wb") as f:
    pickle.dump([prompt, code], f)

  response = {"code": code}
  return jsonify(response)


if __name__ == "__main__":
  app.run(host="0.0.0.0", port=5000, debug=True)
