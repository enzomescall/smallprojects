from PyPDF2 import PdfReader, PdfWriter
import os

def split_pdf(path, output_dir=None):
    """Splits a PDF file into individual pages.

    Args:
        path (str): Path to the PDF file.
        output_dir (str, optional): Directory to save the split pages. 
                                     Defaults to None, saving in the same directory as the input PDF.
    """
    pdf_reader = PdfReader(path)
    num_pages = len(pdf_reader.pages)
    
    file_name = os.path.basename(path).replace('.pdf', '')

    for page_num in range(num_pages):
        pdf_writer = PdfWriter()
        pdf_writer.add_page(pdf_reader.pages[page_num])

        output_filename = f"{file_name}_page_{page_num + 1}.pdf"
        
        if output_dir:
            output_filename = os.path.join(output_dir, output_filename)

        with open(output_filename, 'wb') as output_pdf:
            pdf_writer.write(output_pdf)
        print(f"Created: {output_filename}")

# Example usage:
pdf_path = 'path/to/your/document.pdf' # Replace with your PDF path
output_directory = 'path/to/output/directory' # Optional, replace with desired output directory

split_pdf(pdf_path, output_directory)