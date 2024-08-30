# PATH PLANNING PROJECT

<p>In this project I was working on multi-agent path planning with collision avoidance.</p>
<p>First off I started learning about different algorithms such as: A*, Djisktra, BFS, ILP, CBS and their different variants.</p>
<p>There are a few visualizations in this project, for 2D it only calculates single agent path using A* and visualizes it in pygame. As for 3D visualization I am trying to implement CBS in Blender.</p>

# How to use

## 2D pygame

<p>To visualize agent path planning in 2D, you need to run AStar/heapAStarVisual.py or AStar/SingleAStarVisual.py</p>
<p>First left mouse click defines starting location (green), second defines goal location (red), other times clicking will draw obstacles(grey). Right mouse click is for reseting squares (to white).</p>

<p># Upload picture/video for an example</p>


## 3D Blender

<p>1) Open Blender file visualize.blend</p>
<p>2) Go to scripting and run add_scripts.py</p>
<p>3) In recreate_env.py it is possible to select the amount of agents and range in where it would generate points or it is possible to choose a .json file to read from and spawn points in those locations. These files must be in examples folder.</p>
<p>4) Run main.py scripts. It is possible to choose loc_file as to where to save current points for later to read from that file.</p>
<p>5) Can run the animation.</p>
<p>6) Running Agent_collision.py shows which agents collide in the animation. CBS_collision.py is still under development but it should replan the path when agents collision is detected (Blender might stop responding if agents collide in their start or end locations).</p>

