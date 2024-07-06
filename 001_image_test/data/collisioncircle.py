from data.collisionobject import CollisionObject
import cv2
class CollisionCircle(CollisionObject):
    def __init__(self,**kwargs):
        super(CollisionCircle,self).__init__(**kwargs)
        if 'center' in kwargs and 'radius' in kwargs:
            self.x ,self.y = kwargs['center']
            self.radius = kwargs['radius']

        else:
            raise ValueError("try CollisionCircle(center=(x,y),radius=radius)")
    
    def is_collide(self,point):
        return False

    def get_center(self):
        return self.x, self.y

    def draw_cv(self,image,**options):
        color = (0,255,0)
        thickness = -1 # fill
        linetype = cv2.LINE_AA
        cv_options = {
            'color':color,
            'thickness':thickness,
            'linetype':linetype,
        }
        cv2.rectangle(image,(left,top),(right,bottom),**cv_options)
