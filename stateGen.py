import json

beg2x2 = [
    [0, 1],
    [2, 3]
]
fin2x2Uns =[
    [3, 1],
    [2, 0]
]

beg3x2 =[
    [0,1,2],
    [3,4,5]
]
fin3x2 =[
    [3,4,5],
    [0,1,2]
]

beg3x3 =[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]
beg3x3Uns =[
    [1, 2, 3],
    [4, 5, 6], 
    [7, 8, 0]
]
fin3x3Uns =[
    [7, 8, 6],
    [5, 4, 3], 
    [2, 0, 1]
]
fin3x3D20 =[
    [5, 4, 0], 
    [2, 6, 8], 
    [3, 1, 7]
]
fin3x3D27 = [
    [5, 8, 6], 
    [2, 4, 7], 
    [3, 0, 1]
]
fin3x3D31 =[
    [8, 0, 6], 
    [5, 4, 7], 
    [2, 3, 1]
]

beg4x2 =[
    [0, 1, 2, 3], 
    [4, 5, 6, 7]
]
fin4x2D20 =[
    [2, 7, 6, 5], 
    [1, 0, 3, 4]
]
fin4x2D30 =[
    [0, 3, 1, 5], 
    [7, 2, 6, 4]
]
fin4x2D36 =[
    [3, 2, 5, 4], 
    [7, 6, 1, 0]
]

with open('beg2x2.txt', 'w') as x:
    json.dump(beg2x2, x)
with open('fin2x2Uns.txt', 'w') as x:
    json.dump(fin2x2Uns, x)
with open('beg3x2.txt', 'w') as x:
    json.dump(beg3x2, x)
with open('fin3x2.txt', 'w') as x:
    json.dump(fin3x2, x)
with open('beg3x3.txt', 'w') as x:
    json.dump(beg3x3, x)
with open('beg3x3Uns.txt', 'w') as x:
    json.dump(beg3x3Uns, x)
with open('fin3x3Uns.txt', 'w') as x:
    json.dump(fin3x3Uns, x)
with open('fin3x3D20.txt', 'w') as x:
    json.dump(fin3x3D20, x)
with open('fin3x3D27.txt', 'w') as x:
    json.dump(fin3x3D27, x)
with open('fin3x3D31.txt', 'w') as x:
    json.dump(fin3x3D31, x)
with open('beg4x2.txt', 'w') as x:
    json.dump(beg4x2, x)
with open('fin4x2D20.txt', 'w') as x:
    json.dump(fin4x2D20, x)
with open('fin4x2D30.txt', 'w') as x:
    json.dump(fin4x2D30, x)
with open('fin4x2D36.txt', 'w') as x:
    json.dump(fin4x2D36, x)
