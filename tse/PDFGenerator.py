import PyPDF4

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
