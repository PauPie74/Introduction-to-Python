import pygal
from pygal.style import Style

custom_style = Style(
    colors=('#007aba', '#4d00bb', '#a900ba', '#cf0080', '#cc0025','#be9720','#5bc81f'))

world = pygal.maps.world.SupranationalWorld(style=custom_style)
world.title = 'Paulina Pieper'
world.add('Asia', [('asia', 1,)])
world.add('Europe', [('europe', 1)])
world.add('Africa', [('africa', 1)])
world.add('North america', [('north_america', 1)])
world.add('South america', [('south_america', 1)])
world.add('Oceania', [('oceania', 1)])
world.add('Antartica', [('antartica', 1)])


world.render_to_file("world.svg")