import os
import sys
import json
from PIL import Image
from PIL.ExifTags import TAGS
'''
解决裁剪压缩后的图片Orientation信息不正确问题
'''

def get_exif(im_obj):
    info = im_obj._getexif()
    ret = dict()
    if info:
        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            ret[decoded] = value
    return ret

def get_rotate_degree(im_obj):
    degree = 0
    if hasattr(im_obj, '_getexif'):
        info = im_obj._getexif()
        ret = dict()
        degree_dict = {1: 0, 3: 180, 6: -90, 8: 90}
        if info:
            orientation = info.get(274, 0)
            degree = degree_dict.get(orientation, 0)
    return degree

def get_crop_region(width, height):
    if width < height:
        left = 0
        upper = (height - width) / 2
        right = width
        lower = upper + width
    elif width > height:
        left = (width - height) / 2
        upper = 0
        right = left + height
        lower = height
    else:
        left = 0
        upper = 0
        right = width
        lower = height
    return (left, upper, right, lower)

def list_img_file(directory):
    """列出目录下所有文件，并筛选出图片文件列表返回"""
    old_list = os.listdir(directory)
    # print old_list
    new_list = []
    for filename in old_list:
        name, fileformat = filename.split(".")
        if fileformat.lower() == "jpg" or fileformat.lower() == "png" or fileformat.lower() == "gif":
            new_list.append(filename)
    # print new_list
    return new_list

def generateThumbnail(src_dir, des_dir):
    if not os.path.exists(src_dir):
        os.makedirs(src_dir)
    if not os.path.exists(des_dir):
        os.makedirs(des_dir)
    file_list = list_img_file(src_dir)
    if file_list:
        for infile in file_list:
            im = Image.open(src_dir+infile)
            im = im.rotate(get_rotate_degree(im))
            get_crop_region(im.size[0], im.size[1])
            copy = im.crop(get_crop_region(im.size[0], im.size[1]))
            copy.thumbnail((600, 600))
            copy.save(des_dir+infile, 'JPEG')
            print("successfully compress " + infile)

if __name__ == '__main__':
    generateThumbnail('photos/', 'min_photos/')