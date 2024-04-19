from PIL import Image
##This file contains function to manipulate images
##
##It uses the Icons directory

#function to assemble icons in a single image
def AssemblePalsIcons(palListe):
    path="./"+"_".join(palListe)+".png"
    images = [Image.open("./Icons/"+x+".png") for x in palListe]
    widths, heights = zip(*(i.size for i in images))
    totalWidth = sum(widths)
    maxHeight = max(heights)
    newImage = Image.new('RGBA', (totalWidth, maxHeight))
    separator=Image.open("./Icons/Separation.png")
    x_offset = 0
    for im in images:
        newImage.paste(im, (x_offset,0))
        x_offset += im.size[0]
        if images.index(im)<len(images)-1:
            newImage.paste(separator, (x_offset,0))
            x_offset += separator.size[0]
    newImage.save(path)
    return path

#function to resize the tree image
def ResizeTree(path):
    image = Image.open(path)
    image = image.resize((200,200))
    image.save(path)
    return path