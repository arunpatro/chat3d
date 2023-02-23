# chat3d
interactive text to 3d rendering

## status
- can generate single primitive shapes
- can generate more than one
- generates good objects, llm knows approximate object size
- output code is short because prompts are getting larger, which means we now need to train models, and reduce compute data
- we face competition from https://csm.ai/introducing-coder-text-to-code-for-3d-world-generation-gaming-and-programming/
- https://www.youtube.com/watch?v=zUNS0Ct25RM&t=434s

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

## llm requirements
- should be able to query the scene
- content understanding and reasoning about the scene
  - who is behind whom? 
  - relative to camera? 
  - who owns whom? 
- should be able to modify the parameters of the objects and the scene (RL)


- should start with 2d graphics like svg at first
- can restrict to not too complex shapes like predicting the CSG tree.

## llm core skills
We will develop examples to help the llm learn each skill for scene understanding
- notion of numbers [works n <= 3]
- spatial relative position, prepositionally
- needs to understand material properties

## relevant research
1. Neural Shape Parsers for Constructive Solid Geometry
  - https://arxiv.org/pdf/1912.11393.pdf
  - https://github.com/Hippogriff/3DCSGNet
  - CSG Parsers, can help in generating programs/trees to get the 3D object
  - References are great, can implement some of these
  
2. Object Scene Representation Transformer
  - https://arxiv.org/pdf/2206.06922.pdf
  - related to neural scene representation 

## figma 
- https://www.figma.com/file/maTJrUlXRWfFFuMJqNUywh/chat3d?t=9jl5sPso6Bs0jUjV-0
