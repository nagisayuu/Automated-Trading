import krakenex
k = krakenex.API()
k.load_key('../key/touei.key.test')
volume=k.query_private('Balance', {})
print(volume)
