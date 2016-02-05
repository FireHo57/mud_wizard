from player_object import player_object
from tree_object import tree_object
from game_world import game_world



newPlayer = player_object()
newPlayer.looks_like()
my_game = game_world()

newTree = tree_object()

my_game.register_object( newPlayer )
my_game.register_object( newTree )

newTree.looks_like()
