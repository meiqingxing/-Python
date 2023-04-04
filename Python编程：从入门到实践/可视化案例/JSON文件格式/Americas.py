"""
演示使用Worldmap，突出北美、中美和南美
"""

import pygal

wm = pygal.Worldmap()
wm.title = 'North, Central, and South America'

wm.add("North America", ['ca', 'mx', 'us'])
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])