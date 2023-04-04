"""
演示使用Worldmap，突出北美、中美和南美
"""
import pygal
import pygal_maps_world.maps

wm = pygal_maps_world.maps.World()

wm.title = 'North, Central, and South America'

wm.add("North America", ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'fg', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('Americas.svg')