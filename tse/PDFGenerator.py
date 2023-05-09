from docx import Document
from docx.shared import Inches

document = Document('existing_template.docx')

p = document.add_paragraph("wdwdqdwdqw")

# add the image to the document
image_path = 'Knee_Flexion.png'
image = document.add_picture(image_path)

# get the image dimensions
image_width = image.width
image_height = image.height

# set the position of the image in the page (in EMU)
left = Inches(2)
top = Inches(4)

# set the image size
width = Inches(4)
height = Inches(3)

# set the position and size of the image
image.left = left
image.top = top
image.width = width
image.height = height

p = document.add_paragraph("wdwdqdwdqw")

# add the image to the document
image_path = 'Elbow Flexion.png'
image = document.add_picture(image_path)

# get the image dimensions
image_width = image.width
image_height = image.height

# set the position of the image in the page (in EMU)
left = Inches(2)
top = Inches(4)

# set the image size
width = Inches(4)
height = Inches(3)

# set the position and size of the image
image.left = left
image.top = top
image.width = width
image.height = height

p = document.add_paragraph("wdwdqdwdqw")

# add the image to the document
image_path = 'Pelvis_Flexion.png'
image = document.add_picture(image_path)

# get the image dimensions
image_width = image.width
image_height = image.height

# set the position of the image in the page (in EMU)
left = Inches(2)
top = Inches(4)

# set the image size
width = Inches(4)
height = Inches(3)

# set the position and size of the image
image.left = left
image.top = top
image.width = width
image.height = height



# save the document
document.save('Modified.docx')

