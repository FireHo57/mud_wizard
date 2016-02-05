from abc import ABCMeta

class game_object_base:
    """
    This class is abstract! it makes sure that every (visible) object has
    a looks  like method on it.
    """

    def looks_like(self):
        raise NotImplementedError( "You haven't implemented looks_like()!" )
 
