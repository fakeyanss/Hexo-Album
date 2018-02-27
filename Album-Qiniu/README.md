由于<s>不了解七牛云有没有方便的增量上传</s>（win系统有），所以将要上传的图片和要生成json数据的图片分开存放。

```
-album  
    -photos     存放总的图片，生成json数据
    -min_photos     存放总的压缩图片，生成json数据
-photos     存放将要上传七牛云的图片
-min_photos     存放将要上传七牛云的图片
```

然后对python脚本进行修改，`tool.py`只负责裁剪压缩图片，生成json文件的功能分离出来，放到`make-json.py`,在`handle_photo()`方法中修改json文件生成的地址中。然后每次执行时，按这样的顺序：
1. 加入新的照片到外层`photos`文件夹
2. 运行`python tool.py`，裁剪压缩图片
3. 将新增的照片上传到七牛云
3. 移动外层`photos`和`min_photos`文件夹下的图片到`album`下的对应文件夹中
4. 运行`python make-json.py`，生成json文件

> 批量上传到七牛云，脚本是`upload-files-to-load.py`，在里面配置密匙和buckey存储空间名，用法`python upload-files-to-load.py a/ dir`，可以把本地dir路径下的文件（dir可以是文件夹）上传到对应bucket下，并且前缀是`a/`。

为了避免每次都手动操作，写了一个批处理程序`auto.sh`，可以修改里面的文件夹地址，然后双击运行。如果是mac，可以将后缀名改为`.command`，然后设置可执行权限`chmod 777 auto.command`，即可双击运行。

如果要相片不限制为正方形，可以任意尺寸，参照[我正在用的设置](https://github.com/fakeYanss/Blog_Album)
