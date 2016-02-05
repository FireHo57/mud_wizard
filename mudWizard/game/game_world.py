'''
This object represents the game world
'''

class game_world:

    def __init__( self ):
        #doesn't have to be intialized with anything
        self._no_game_objects=0
        self._game_objects=[]
        print( "Game created!" )

    def register_object( self , game_object_base ):
        self._game_objects.append( ( self._no_game_objects , game_object_base )  )
        print("Registered as {}".format( self._no_game_objects ) )
        self._no_game_objects+=1

'''
    def deregister_object( self , object_id ):
        self._game_objects.pop( object_id )
        for( i : )
'''


