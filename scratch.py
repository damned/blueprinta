from openpyxl import load_workbook
import svgwrite

wb=load_workbook('blueprint.xlsx')
sheet=wb.active
a9=sheet['A9']

dwg = svgwrite.Drawing('blueprint.svg', profile='tiny', size=(800, 600))
dwg.add(dwg.rect((0, 0), (100, 80), fill='lightblue'))
text = dwg.text(a9.value, insert=(5, 25), fill='black', font_family='sans')
print(f'text {text}')
dwg.add(text)
words = str(a9.comment).split(' ')
y = 40
for word in words:
    dwg.add(dwg.text(word, insert=(20, y), fill='black', font_family='sans'))
    y += 10

dwg.save()

print(a9.value)
print(a9.comment)
