from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = "Ameryka Północna, Środkowa i Południowa"

wm.add('Ameryka Północna', ['ca', 'us', 'mx'])
wm.add('Ameryka Środkowa', ['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('Ameryka Południowa', ['ar', 'bo', 'br', 'cl',
                              'co', 'ec', 'gf', 'gy', 'pe', 'py', 'sr', 'uy', 've'])


wm.render_to_file('Data Mining/americas.svg')
