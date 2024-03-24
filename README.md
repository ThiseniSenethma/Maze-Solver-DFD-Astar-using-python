# A maze solver implemented using Depth First Search (DFS) and A star (A*) search algorithms 

## The maze :
    
  <ui>
    <li> has (x, y) coordinates of each node defined by the column and the row shown at the top and left of the maze, respectively. 
    For example, node 15 has (x, y) coordinates (2, 3) </li>
    <li> has a start node randomly selected within the 0-11 nodes </li>
    <li>  has a goal node randomly selected within the 24-35 nodes </li>
    <li> randomly select four barrier nodes from the remaining 34 nodes in the maze. </li>
    </ui>
  
## Moves
 <ui>
    <li>Only valid moves are going horizontal, vertical and diagonal</li>
    <li>No moves are allowed through the barrier nodes</li>
 </ui>

 ### DFS
 <ui>
    <li> Process neighbors in increasing order. For example, if processing the neighbors of node 8 , first process 2, then 7, then 9, then 14 </li>
 </ui>

 ### A star
 <ui>
 <li>Calculate heuristic cost </li>
 </ui>
