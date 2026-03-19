# Megaminx-Solver
A megaminx cube built in python, solved with the A* algorithm.

for i = 3 to i = 11\
Randomly turns a face on the cube i times, solves with A*, outputs all cube faces to check if solved and time taken.

Heuristic is equal to the number of faces mismatched divided by 15; 5 corners + 5 edges + 5 side-edges;
