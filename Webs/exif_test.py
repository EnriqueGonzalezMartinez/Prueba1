import os
from exif import Image

ls = os.listdir('C:\\Users\\Adrian\\Pictures')
names = ['C:\\Users\\Adrian\\Pictures\\'+x for x in ls if x.endswith('.jpg')]

for name in names:
    with open(name,'rb') as file:
        img = Image(file)
        if img.has_exif:
            attributes = dir(img)
            
