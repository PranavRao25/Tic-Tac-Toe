# Tic-Tac-Toe
This is an individual mini-project as a Lab project for CS2180 Artificial Intelligence Lab.

The main algorithm is MiniMax algorithm with Alpha-beta Pruning.

MiniMax algorithm is an Adverserial Search algorithm which traverses through the game tree (of alternating Min-Max nodes) and selects the best course of moves.
Alpha-Beta Pruning is an improvement over standard (or Vanilla) MiniMax algorithm, where it cuts off unnecessary branches of the game tree thus reducing the running time of the algorithm.

The underlining assumption is that the user plays optimally, however in the case of the suboptimal play by the user, the end-result is simply delayed.

The user can start his play with either X/O on any of the tiles, and the game can either end in a draw or win of the AI.
