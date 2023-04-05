"""
演示使用Worldmap，突出北美、中美和南美
"""
# import pygal  # 以前版本的代码
import pygal_maps_world.maps  # 如今使用


wm = pygal_maps_world.maps.World()
wm.title = 'North, Central, and South America'

wm.add("North America", {'ca': 3412600, 'mx': 113423000, 'us': 30934900})  # add一个标签和字典（包含国家的国别码和人口数量）
wm.add('Central America', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add("South America", ['ar', 'bo', 'br', 'cl', 'co', 'ec', 'fg', 'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('Americas.svg')  # 创建一个包含该图表的.svg文件；以不同颜色突出北美、中美、南美


