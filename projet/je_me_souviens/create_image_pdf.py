from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
import os

def create_image_pdf():
    # Directory containing the images
    image_dir = "/Users/jbarbeau/Sites/artist-docs/projet/je_me_souviens/dossier_visuel"
    output_pdf = "/Users/jbarbeau/Sites/artist-docs/projet/je_me_souviens/image_catalog.pdf"

    # Create a new PDF
    c = canvas.Canvas(output_pdf, pagesize=A4)
    width, height = A4

    # Get all PNG files and sort them
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]
    image_files.sort()

    for image_file in image_files:
        # Extract title from filename (remove number prefix and replace underscores with spaces)
        title = ' '.join(image_file.split('_')[1:]).replace('.png', '')

        # Add image (larger and centered)
        img_width = width - 2*inch  # leave 1 inch margin on each side
        img_height = height - 3*inch  # leave space for title at bottom
        x = (width - img_width) / 2
        y = (height - img_height) / 2 + 0.5*inch  # shift up a bit for title
        image_path = os.path.join(image_dir, image_file)
        c.drawImage(image_path, x, y, width=img_width, height=img_height, preserveAspectRatio=True, anchor='c')

        # Add title
        c.setFont("Helvetica-Bold", 18)
        c.drawCentredString(width / 2, 1*inch, title)

        # Add new page
        c.showPage()

    # Save the PDF
    c.save()

if __name__ == "__main__":
    create_image_pdf()