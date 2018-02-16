---
title: Photos
date: 2017-12-29 22:32:22
type: "photos"
comments: false
---
<link rel="stylesheet" href="./ins.css">
 <link rel="stylesheet" href="./photoswipe.css"> 
<link rel="stylesheet" href="./default-skin/default-skin.css"> 
<div class="photos-btn-wrap">
  <a class="photos-btn active" href="javascript:void(0)" target="_blank" rel="external">Photos</a><a class="photos-btn" target="_blank" href="http://wp.yanss.top/" style="color:#08c; border-bottom:1px #999">Gallery</a>
</div>
<div class="instagram itemscope">
  <a href="http://blog.yanss.top" target="_blank" class="open-ins">图片正在加载中…</a>
</div>

<script>
  (function() {
    var loadScript = function(path) {
      var $script = document.createElement('script')
      document.getElementsByTagName('body')[0].appendChild($script)
      $script.setAttribute('src', path)
    }
    setTimeout(function() {
        loadScript('./ins.js')
    }, 0)
  })()
</script>