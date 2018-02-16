# -*- coding: utf-8 -*-

import os
import sys
from qiniu import Auth, put_file
'''
if 3 != len(sys.argv):
    print('[Usage] %s [dir_set] [filepath]' % os.path.basename(sys.argv[0]))
    sys.exit(0)
'''
if 2 == len(sys.argv):
	dir_set = ''
	file_path = sys.argv[1]
else:
    dir_set = sys.argv[1] # dir_set 的格式为 image/upload-qiniu/ ，注意末尾带反斜杠/
    file_path = sys.argv[2]

access_key = 'xxxxxxx' # 个人中心->密匙管理->AK
secret_key = 'xxxxxxx' # 个人中心->密匙管理->SK

bucket_name = 'photos' # 七牛空间名
bucket_url = {
    "photos": "xxxxxx.bkt.clouddn.com",
    "blog-source": "xxxxxx.bkt.clouddn.com",
}
qiniu_auth = Auth(access_key, secret_key)

def upload_qiniu(input_path):
    #upload single file to qiniu
    filename = os.path.basename(input_path)
    key = '%s%s' % (dir_set, filename)

    token = qiniu_auth.upload_token(bucket_name, key)
    ret, info = put_file(token, key, input_path, check_crc=True)
    if ret and ret['key'] == key:
        print('%s done' % (bucket_url[bucket_name] + '/' + dir_set + filename))
    else:
        print('%s error' % (bucket_url[bucket_name] + '/' + dir_set + filename))

def upload_all_files(input_path):
    if os.path.isfile(input_path):
        upload_qiniu(input_path)
    elif os.path.isdir(input_path):
        dirlist = os.walk(input_path)
        for root, dirs, files in dirlist:
            for filename in files:
                upload_qiniu(os.path.join(root, filename))
    else:
        print('Please input the exists file path!')

if __name__ == "__main__":
    upload_all_files(file_path)
