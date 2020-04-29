import numpy as np

def get_scaling_image_affine(src_size,dst_size,scale_type=None):
    print(src_size)
    src_width,srs_height = src_size
    dst_width,dst_height = dst_size
    x_scale = dst_width / src_width
    y_scale = dst_height / srs_height
    x_offset = 0
    y_offset = 0
    if x_scale > y_scale:
        x_scale = y_scale
        x_offset = (dst_width - src_width * x_scale) / 2
    else:
        y_scale = x_scale
        y_offset = (dst_height - srs_height * y_scale) / 2
    affile_mat = np.array([[x_scale,0,x_offset],[0,y_scale,y_offset]],np.float32)
    return affile_mat

def get_scaling_affine(src_size,dst_size,scale_type=None):
    print(src_size)
    src_width,srs_height = src_size
    dst_width,dst_height = dst_size
    x_scale = dst_width / src_width
    y_scale = dst_height / srs_height
    x_offset = 0
    y_offset = 0
    affile_mat = np.array([[x_scale,0,x_offset],[0,y_scale,y_offset]],np.float32)
    return affile_mat

