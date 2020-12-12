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

print(f'Part 1: {ans}')


# PART 2
layer = [list(layer) for layer in layers]
pixel_by_layer = list(zip(*layer)) # * changes the elements in the list into separate arguments

image = ''
for pixel in pixel_by_layer:
    color = None
    for ch in list(pixel):
        if ch != '2':
            color = ch
            break
    if color is None:
        color = '2'
    image += color

image = textwrap.wrap(image, width)

print('Part 2: ')
for row in image:
    print(row.replace('0','.'))
