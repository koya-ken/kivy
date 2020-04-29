from event.clickevent import ClickEvent
from utils.affine import get_scaling_affine
from utils.affine import get_scaling_image_affine
import numpy as np
import cv2

class ImageClickEvent(ClickEvent):
    def __init__(self,**kwargs):
        super(ImageClickEvent,self).__init__(**kwargs)
        self.image_size = kwargs['image_size']
    def convert_local_point(self,widget,touch):
        # 画像領域を座標として扱う
        x,y = widget.to_local(*touch.pos)
        # kivyの原点が左下になっているので左上に揃える
        y = self.widget_size[1] - y
        point = np.array([x,y,1]).reshape(-1,1)
        # クリック座標をオリジナルのサイズに変換する
        point = np.dot(self.invert_view_port_affine,point)
        point = np.vstack([point,[1]])
        # オリジナルのサイズから画像の相対座標に変換する
        point = np.dot(self.invert_view_affine,point)
        image_point = point.flatten().astype(np.int64)
        return image_point
    def update_widget_size(self,wiget,widget_size):
        texture_size = wiget.texture_size
        self.widget_size = widget_size
        self.image_size = texture_size

        view_affine = get_scaling_image_affine(self.image_size,self.widget_size)
        original_view_size = np.array(self.widget_size) * (1/view_affine[0][0])
        # 画像がオリジナルのサイズの状態でセンタリングしたときのアフィン行列を取得
        original_image_view_affine = get_scaling_image_affine(self.image_size,original_view_size)
        self.invert_view_affine = cv2.invertAffineTransform(original_image_view_affine)
        self.invert_view_port_affine = get_scaling_affine(self.widget_size,original_view_size)
        self.original_view_size = original_view_size
