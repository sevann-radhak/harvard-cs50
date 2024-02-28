from fpdf import FPDF

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.add_page()
pdf.set_font("helvetica", "B", 16)

pdf.cell(200, 10, "CS50 Shirtificate", 0, 1, 'C')

pdf.image("./shirtificate.png", x=10, y=20, w=190)
pdf.set_text_color(255, 255, 255)  
pdf.set_xy(10, 60)
pdf.cell(200, 10, "Sevann Radhak", 0, 0, 'C')  

pdf.output("shirtificate.pdf")