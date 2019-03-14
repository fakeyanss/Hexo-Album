#! /usr/bin/python
# -*- coding: utf-8 -*-

from qiniu import Auth, put_file
from qiniu import BucketManager
import sys
import os

# 配置七牛云信息
access_key = "N46By9onEdAUSfBygEj7HDN-zCGStVdtd5LLkw3U"
secret_key = "Awoknf4sGtrcCAztGFjolZo_F3P8SDlKCAyLn-g3"
bucket_name = "blog"
bucket_url = {
    "photos": "photo.yanss.top",
    "blog": "pic.yanss.top"
}
md_url_result = "md_path.txt"


def upload_img(bucket_name, file_name, file_path):
    # generate token
    token = q.upload_token(bucket_name, file_name, 3600)
    put_file(token, file_name, file_path)


def get_img_url(bucket_url, file_name):
    img_url = 'http://%s/%s' % (bucket_url, file_name)
    # generate md_url
    imageName = file_name.split('.')
    if imageName[1].lower() == 'jpg' or imageName[1].lower() == 'png' or imageName[1].lower() == 'jpeg' or imageName[1].lower() == 'bmp' or imageName[1].lower() == 'gif':
        md_url = "![%s](%s)\n" % (imageName[0], img_url)
    else:
        md_url = "[%s](%s)\n" % (imageName[0], img_url)
    return md_url


def save_to_txt():
    # save md_url to txt
    with open(md_url_result, "a", encoding="utf-8") as f:
        f.write(url_before_save)
    return


# 保存进剪贴板
def addToClipBoard(text):
    command = 'echo ' + text.strip() + '| clip'
    os.system(command)


if __name__ == '__main__':
    q = Auth(access_key, secret_key)
    bucket = BucketManager(q)
    # 获取传过来的路径数组
    imgUrls = sys.argv[1:]
    # 遍历数组进行文件上传
    for imgUrl in imgUrls:
        # 获取文件名
        up_filename = os.path.split(imgUrl)[1]
        # 上传图片至七牛云
        upload_img(bucket_name, up_filename, imgUrl)
        # 保存进系统剪贴板
        print("upload success : %s " % up_filename)
        url_before_save = get_img_url(bucket_url[bucket_name], up_filename)
        addToClipBoard(url_before_save)
        # 写进文本文件
        save_to_txt()
