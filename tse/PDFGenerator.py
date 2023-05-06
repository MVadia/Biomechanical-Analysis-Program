import PyPDF4
from PIL import Image
import io
# Open the existing PDF file in read-binary mode
with open('existing_template.pdf', 'rb') as existing_file:

    # Create a new PDF file in write-binary mode
    with open('output.pdf', 'wb') as new_file:

        # Create a PDF reader object for the existing file
        reader = PyPDF4.PdfFileReader(existing_file)

        # Create a PDF writer object for the new file
        writer = PyPDF4.PdfFileWriter()

        # Select the first page of the existing file
        page = reader.getPage(0)

        # Add the page to the writer object
        writer.addPage(page)

        # Write the writer object to the new file
        writer.write(new_file)


# Open the existing PDF file in read-binary mode
with open('output.pdf', 'rb') as existing_file:

    # Create a PDF reader object for the existing file
    reader = PyPDF4.PdfFileReader(existing_file)

    # Create a PDF writer object
    writer = PyPDF4.PdfFileWriter()

    # Open the image file
    with Image.open('Knee_Flexion.png') as img:

        # Get the first page of the existing PDF file
        existing_page = reader.getPage(0)

        # Create a new blank page object
        img_page = PyPDF4.pdf.PageObject.createBlankPage(
            None, img.width, img.height)

        # Add the image to the new page object
        img_page.addImage(img, 0, 0, img.width, img.height)

        # Calculate the scale factor based on the image size and the PDF page size
        scale_x = img.width / float(existing_page.mediaBox.getWidth())
        scale_y = img.height / float(existing_page.mediaBox.getHeight())

        # Merge the image page with the existing PDF page
        existing_page.mergeTranslatedPage(
            img_page, tx=0, ty=0, expand=False)

        # Add the modified page to the writer object
        writer.addPage(existing_page)

    # Add the rest of the pages from the existing file to the writer object
    for i in range(1, reader.getNumPages()):
        writer.addPage(reader.getPage(i))

    # Overwrite the input file with the modified PDF
    with open('output.pdf', 'wb') as output_file:
        writer.write(output_file)