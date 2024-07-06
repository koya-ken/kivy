from event.clickeventcode import ClickEventCode
import numpy as np
class ClickEvent:
    point = None
    pre_point = None
    button = None
    widget_size = None
    def __init__(self,**kwargs):
        self.widget_size = kwargs['widget_size']
    def convert_local_point(self,widget,touch):
        x,y = widget.to_local(*touch.pos)
        # 左上原点
        return x, self.widget_size[1] - y
    def update(self,code,widget,touch):
        self.code = code
        self.pre_point = self.point
        self.point = self.convert_local_point(widget,touch)
        self.button = touch.button
    def update_widget_size(self,widget,size):
        self.widget_size = size
    def get_point(self):
        return self.point
    def get_button(self):
        return self.button
    def get_delta(self):
        if self.pre_point is None:
            return [0,0]
        return np.array(self.point) - np.array(self.pre_point)