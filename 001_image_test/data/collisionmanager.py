from data.collisionobject import CollisionObject
class CollisionManager(CollisionObject):
    def __init__(self,**kwargs):
        super(CollisionManager,self).__init__(**kwargs)

    def add_collision(self,id,collision,layer=None):
        pass
    def remove_collision(self,id):
        pass
    def get_collision(self,id):
        pass
    def get_collide_collision(self,touch):
        pass
    def fire_mouse_event(self,event):
        pass