# chat3d
interactive text to 3d rendering

## features
- want a cool minimal 3d editor that you can chat with. 
- custom chat model, should ideally be a small one, edge deployable?
- has read the documentation to pretrain on a subset of libraries
- more specific than generic to the tool (to constrain it)

## challenges
- model makes generative errors, doesn't match the exact code that sometimes works
- sometimes output is not correct, sometimes not complete, sometimes redundant
- how to verify and also correct the output? 
- logic to verify can be to have input output templates, and define what it means to be reliable
- reliable means to have verify that each component of the rendering scene is present and logical structures are held

## expts
- multiple llm model
- break down task -> generate code for each task -> verify each code -> tie it all up
- better to finetune the model than do prompt engineering. Prompts can be rather used to choose the type of the task perhaps? 
- how to use agents to handle the multiple llm model? 
