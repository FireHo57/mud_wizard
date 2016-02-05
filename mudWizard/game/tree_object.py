from game_object_base import game_object_base

class tree_object(game_object_base):
    def __init__(self):
        print("I am a tree!")

    def looks_like(self):
        print("A glorious maplewood with orangey leaves and silver bark. In the branches you can see squirrels and an owl who is asleep")
