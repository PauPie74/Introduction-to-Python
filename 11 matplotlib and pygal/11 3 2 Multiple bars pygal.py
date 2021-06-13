import pygal
from pygal.style import Style

custom_style = Style(
    opacity = 1.0,
    colors=('green','red'))

line_chart = pygal.Bar(style=custom_style, width=700)
line_chart.title = 'Title'
line_chart.x_labels = ['G1','G2','G3','G4','G5']
line_chart.add("Men", [22, 30, 34, 30, 27])
line_chart.add("Women",  [25, 32, 30, 35, 29])

line_chart.render_to_file("chart.svg")