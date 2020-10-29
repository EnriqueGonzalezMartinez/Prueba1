from PIL import ExifTags, Image
from PIL.ExifTags import TAGS, GPSTAGS

# Crear una imagen en blanco, de dimensiones 800x400
#img = Image.new('RGBA', (800, 400), 'white')
#img.save('image.png')
# Listar metadatos de la imagen

# path to the image or video
imagename = "c:/Users/Adrian/Pictures/hola.jpg"
# read the image data using PIL
image = Image.open(imagename)
# After reading the image using Image.open() function, 
# let's call the getexif() method on the image which returns image metadata
exifdata = image.getexif()
# The problem with exifdata variable now is that the field 
# names are just IDs, not a human readable field name, 
# that's why we gonna need the TAGS dictionary from PIL.ExifTags 
# module which maps each tag ID into a human readable text
for tag_id in exifdata:
    # get the tag name, instead of human unreadable tag id
    tag = TAGS.get(tag_id, tag_id)
    data = exifdata.get(tag_id)
    # decode bytes 
    if isinstance(data, bytes):
        data = data.decode()
    print(f"{tag:25}: {data}")