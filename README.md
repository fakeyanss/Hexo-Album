* # Hexo博客添加相册
* <a href="http://foreti.me/archives/14046165.html#album">原理及相关设置</a>
* 这里有两种选择，以github仓库做图床或者以七牛云做图床，分别在`Album-Github`和`Album-Qiniu`文件夹中有详细内容
* 图片上传到github并裁剪压缩，脚本是`ImageProcess.py`和`tool.py`，运行`tool.py`即可压缩生成图片并上传github（用七牛云做相册源可以注释git上传 ），需要在`handle_photo()`方法中修改data.json输出地址。

> 使用七牛云做图床需要先安装python3.6环境，然后安装七牛SDK Python版`pip install qiniu`
