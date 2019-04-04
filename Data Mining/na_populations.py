from pygal.maps.world import World

wm = World()
wm.force_uri_protocol = 'http'
wm.title = "Wielkość populacji w krajach Ameryki Północnej"
wm.add('Ameryka Północna', {'ca': 34126000, 'us': 309349000, 'mx': 113423000})

wm.render_to_file('Data Mining/na_populations.svg')
