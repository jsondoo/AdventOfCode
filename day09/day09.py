import textwrap
import collections

from itertools import permutations

with open('input.txt', 'r') as file:
    text = file.read()

# PART 1
width, height = 25, 6
layer_size = width * height

layers = textwrap.wrap(text, layer_size) # split
mini = float('inf')
ans = None
for layer in layers:
    c = collections.Counter(layer)
    if c['0'] < mini:
        mini = c['0']
        ans = c['1'] * c['2']

print('ans ', ans)
print(layers) # list of strings

lay = [list(layer) for layer in layers]
zipped = list(zip(*lay))

# PART 2
image = ''
for z in zipped:
    reee = None
    for ch in list(z):
        if ch != '2':
            reee = ch
            break
    if reee is not None:
        image += reee
    else:
        image += '2'

image = textwrap.wrap(image, 25)
print(image)

for layer in image:
    print(layer.replace('0','.'))
