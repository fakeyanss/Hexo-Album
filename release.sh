#!/bin/bash
cd /Users/yanss/Documents/Blog/Blog_Album
#删除占位文件
rm -f -v /Blog_Album/photos/README.md
rm -f -v /Blog_Album/min_photos/README.md
#生成缩略图
python compress.py
#上传新图片
python upload-files-to-qiniu.py photos/
python upload-files-to-qiniu.py min_photos/ /min_photos/
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