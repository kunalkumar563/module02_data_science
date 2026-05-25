from reportlab.pdfgen import canvas

pdf = canvas.Canvas("students.pdf")

pdf.drawString(100, 750, "Name: Kunal")
pdf.drawString(100, 730, "Marks: 85")

pdf.save()

print("PDF Created")