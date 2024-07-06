from data.collisionobject import CollisionObject
import cv2
class CollisionRectangle(CollisionObject):
    def __init__(self,**kwargs):
        super(CollisionRectangle,self).__init__(**kwargs)
        if 'rect' in kwargs:
            rect = kwargs['rect']
            self.left,self.top,self.width,self.height = rect
            self.right = self.left + self.width
            self.bottom = self.top + self.height
        elif 'center' in kwargs and 'size' in kwargs:
            self.width,self.height = kwargs['size']
            center_x,center_y = kwargs['center']
            self.left = int(center_x - self.width / 2)
            self.top = int(center_y - self.height / 2)
            self.right = self.left + self.width
            self.bottom = self.top + self.height
        else:
            raise ValueError("try CollisionRectangle(rect=(left,top,width,height)) or CollisionRectangle(center=(x,y),size=(width,height))")
    
    def is_collide(self,point):
        x,y = point
        if x < 0 or x > self.width:
            return False
        if y < 0 or y > self.height:
            return False
        return True
    
    def get_point(self):
        return self.left,self.top

    def get_center(self):
        center_x = self.left - self.width / 2
        center_y = self.top - self.height / 2
        return center_x,center_y

    def draw_cv(self,image,**options):
        left = self.left
        top = self.top
        right = self.right
        bottom = self.bottom
        color = (0,255,0)
        thickness = -1 # fill
        linetype = cv2.LINE_AA
        cv_options = {
            'color':color,
            'thickness':thickness,
            'linetype':linetype,
        }
        cv2.rectangle(image,(left,top),(right,bottom),**cv_options)
