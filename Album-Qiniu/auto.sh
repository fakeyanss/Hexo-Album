cd C:/Users/yanss/Desktop/HexoAlbum/Album-Qiniu &&\
python tool.py && \
python upload-files-to-qiniu.py photos && \
python upload-files-to-qiniu.py min_photos/ min_photos && \
mv C:/Users/yanss/Desktop/HexoAlbum/Album-Qiniu/photos/* album/photos && \
mv C:/Users/yanss/Desktop/HexoAlbum/Album-Qiniu/min_photos/* album/min_photos && \
python make-json.py