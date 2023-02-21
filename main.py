from flask import Flask, request, jsonify, render_template
from langchain.llms import OpenAI
from langchain import PromptTemplate, FewShotPromptTemplate
from sample_objects import examples, mickey_mouse, a_small_blue_ball

app = Flask(__name__, template_folder="templates", static_folder="static")
model = OpenAI(
    temperature=0.5,
    openai_api_key="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",
)

template = """
Description: {description}
Code: {code}\n
"""

prefix="""I want you to generate the code for three.js to generate one or more 3d models. We need code for four things: 1. Objects 2. Camera 3. Scene 4. Lights. 
Given a description of the object, your task is to generate the code for the object and if neccessary group the objects to create a composite group object.
Return the code as a string without any docstrings or english text, which will directly executed on the js console.
Here are a few examples of how to do this:"""

suffix="Description: {description}\nCode:"

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

# Index page (now using the index.html file)
@app.route("/")
def index():
    return render_template("index.html")


# from sample_objects import mickey_mouse, ball

# print(mickey_mouse)
render_code = """
function animate() {
  requestAnimationFrame(animate);
  //ball.rotation.y += 0.01;
  renderer.render(scene, camera);
}
// Call the animation function
animate();
"""

@app.route("/generate", methods=["POST"])
def generate():
    prompt = request.json["prompt"]
    print("Generating code for prompt: ", prompt)
    # code = ball
    # code = model(prompt_builder.format(input=prompt))
    # code += render_code
    code = a_small_blue_ball
    print(code)
    response = {"code": code}
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
