from fpdf import FPDF
import os, math
#210 x 297 mm

#74.25
#148.5
#222.75


pdf = FPDF( 'P', 'mm', 'A4')
pdf.add_font("Japanese", "", "Japanese.ttf", uni=True)
pdf.set_font("Japanese", size = 20)


with open("input.txt", encoding="utf8") as f:
    lines = f.readline()

lines = lines.replace('-', '/')
lines = lines.split("/")

totallines=len(lines)
totalcards=totallines/2
pages=math.ceil(totalcards/4)

for x in range(0,pages):
    pdf.add_page()
    #vertical line
    pdf.dashed_line(105, 0, 105, 297, dash_length = 1, space_length = 1)
    #3 horizontal lines
    pdf.dashed_line(0, 74.25, 210, 74.25, dash_length = 1, space_length = 1)
    pdf.dashed_line(0, 148.5, 210, 148.5, dash_length = 1, space_length = 1)
    pdf.dashed_line(0, 222.75, 210, 222.75, dash_length = 1, space_length = 1)
    #creates cells sized 105x 74.25mm

    #cell1
    pdf.set_y(0)
    pdf.cell(-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)], 0, 1, 'C')
    except:
        pass

    #cell2
    pdf.set_y(0)
    pdf.cell(105-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+1], 0, 1, 'C')
    except:
        pass

    
    #cell3
    pdf.set_y(74.25)
    pdf.cell(-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+2], 0, 1, 'C')
    except:
        pass

    #cell4
    pdf.set_y(74.25)
    pdf.cell(105-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+3], 0, 1, 'C')
    except:
        pass

        #cell5
    pdf.set_y(148.5)
    pdf.cell(-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+4], 0, 1, 'C')
    except:
        pass

    #cell6
    pdf.set_y(148.5)
    pdf.cell(105-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+5], 0, 1, 'C')
    except:
        pass


    #cell7
    pdf.set_y(202)
    pdf.cell(-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+6], 0, 1, 'C')
    except:
        pass

    #cell8
    pdf.set_y(202)
    pdf.cell(105-10)
    try:
        pdf.cell(105, 74.25, lines[(x*8)+7], 0, 1, 'C')
    except:
        pass




pdf.output("Output.pdf")
os.startfile("Output.pdf")