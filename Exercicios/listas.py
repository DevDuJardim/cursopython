bands = []
print(bands)
bands.append('metallica')
print(bands)
bands.append('Slayer')
print(bands)
bands.append('anthrax')
print(bands)
bands[2] = 'ratos de porão'#troca
print(bands)
bands.append('sandy & junior')#acresenta
print(bands)
bands.insert(2,'bob marley')
print(bands)
del bands[0]
print(bands)

popped_bands = bands.pop()
print(bands)
print(popped_bands)
bands.remove('ratos de porão')
print(bands)