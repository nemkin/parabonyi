import math
from scipy.sparse import rand

def to_char(num):
  return chr(ord('A') + num)

n = 6
o_x = 1
o_y = 1



print('\\begin{center}')
print('\\begin{tikzpicture}[scale=2]')

for i in range(n):
  angle = 360 // n * i 
  c = to_char(i)
  x = o_x + math.cos(angle)
  y = o_y + math.sin(angle)
  print(f'\coordinate ({c}) at ({x:.2f},{y:.2f});')


edges = rand(n, n, density=0.5)

for i,j in zip(edges.row, edges.col):
  print(f'\draw[thick] ({to_char(i)}) -- ({to_char(j)});');

for i in range(n):
  print(f'\draw[thick, fill=white] ({to_char(i)}) circle (0.2) node {to_char(i)};')

print('\\end{tikzpicture}')
print('\\end{center}')

