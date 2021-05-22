import pygal
from pygal.style import Style

custom_style = Style(
    colors=('#007aba', '#4d00bb', '#a900ba', '#cf0080', '#cc0025','#be9720','#5bc81f'))

line_chart = pygal.Line(style=custom_style)
line_chart.title = 'Paulina Pieper'
line_chart.y_labels = [0.0001,0.0003,0.0004,0.00045,0.0005]
line_chart.add('line',  [0.0002,0.0005,0.00035])
line_chart.render_to_file("bar_chart.svg")