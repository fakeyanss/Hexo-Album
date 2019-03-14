# Hexo博客添加相册
* [原理及相关设置](https://foreti.me/2017/12/31/hexo-next-personal/#album)

## 使用七牛云图床
> 使用七牛云做图床需要先安装python3.6环境，然后安装七牛SDK Python版`pip install qiniu`

* 文件夹结构. album下的内容, 存放所有的图片. 外层photos中存放新增的图片，用于上传七牛云。上传完后会将移动到albums下，并生成json文件。

```
├─album
│  ├─min_photos
│  └─photos
├─photos
└─min_photos
```

* 添加新图片后的提交命令. `release.sh`
```sh
#!/bin/bash
cd /Users/yanss/Documents/Blog/Blog_Album
#删除占位文件
rm -f -v /Blog_Album/photos/README.md
rm -f -v /Blog_Album/min_photos/README.md
#生成缩略图
python compress.py
#上传新图片
python upload-files-to-qiniu.py photos/
python upload-files-to-qiniu.py min_photos/ min_photos/
#移动新图片到album下
if [ "`ls photo/`" != "" ]; then
  mv photos/* album/photos/ 
fi
if [ "`ls min_photos/`" != "" ]; then
  mv min_photos/* album/min_photos/
fi

#生成json文件
python make-json.py
#压缩备份album文件夹
python zip.py
#上传压缩文件（可以不用每次都上传）
python upload-files-to-qiniu.py album.zip
#生成占位文件
echo "这是一个占位文件！" > photos/README.md
echo "这是一个占位文件！" > min_photos/README.md

#上传到远程git仓库
git add .
git commit -m "add photos"
git push origin master
```

* 以下是两个独立的上传图片到七牛的功能
    * Feature: 拖拽单文件上传到[七牛云](https://portal.qiniu.com/create)并返回markdown格式外链, 脚本是`upload-a-file-to-qiniu(md).py`, 修改`access_key`, `secret_key`, `bucket`等参数后运行`python upload-a-file-to-qiniu(md).py filename`即可，filename为待上传file路径，window环境下可以将图片拖拽到`drag-file-on-me.bat`上直接运行.
    * Feature: 批量上传到七牛云，脚本是`upload-files-to-qiniu.py`, 用法`python upload-files-to-qiniu.py a/ dir`,  可以把本地dir路径下的文件(dir可以是文件夹)上传到对应bucket下，并且前缀是`a/`.


* 若要上传视频，会比较麻烦，有以下步骤。
  1. 对视频片段截图，作为视频封面，图片名和视频名相同
  2. 将封面图片作为普通照片压缩、上传、移动到/album
  3. 将视频上传
  4. 在/album/photos/中删除封面图片，将视频文件移动到此目录下
  5. 运行make-json.py