#for i in *;do convert $i $i.jpg; done

import numpy as np
import cv2
files = glob.glob("*.jpg")
for f in files:
    img=cv2.imread(f,0)
    out = file(f+'.mat','w')
    out.write(str(img.shape[0]*img.shape[1])+'\n')
    out.write('1\n')
    for i in img:
        for j in i:
            out.write(str(j)+'\n')

out = file('all.mat','w')
out.write(str(len(files))+'\n77760\n')
for f in files:
    img=cv2.imread(f,0)
    for i in img:
        for j in i:
            out.write(str(j)+'\n')
out = file('labels.mat','w')

for f in files:
    out.write(f+'\n')

