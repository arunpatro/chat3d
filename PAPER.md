# how well do llms understand a scene? 
We want to understand how well AI can help in generating arbitrary complex 3D models? 

## Introduction
A geometric model can be represented explicitly by triangle-based meshes or implicitly using SDFs or shapes. There is considerable literature capturing both types. We first review the literature to generate explicit structures and then implicit ones. 

Explicit:
- Meshes can be easily rendered using rasterization. They are expensive to store, as they represent a hashtable of precomputed values. 
- NeRFs ??

Implicit:
- PiFU, and other papers also talk about this

Most methods have studied generating only single objects. In this paper we discuss AI 3D generation in a general setting where we predict the entire scene graph, which is composed of multiple objects and are in relation to each other. We experiment with llms in a variety of tasks in scene understanding. This enables them to generate multiple objects in heirarachy to each other. This is primarily a vector scene representation effort useful in industries like CAD Manufacturing. 

## Scene Graphs
A scene graph is heirarchial tree representation of objects with the root being the scene object. All objects are parent child relationships to and can represent either groups or parts. 

Rendering a scene graph should be very trivial and we should be able to efficient three js code from it. IMO the scene graph is the smallest representation of the scene, that the llm needs to figure out. 

