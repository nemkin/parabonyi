import math
from scipy.sparse import rand

def to_char(num):
  return chr(ord('A') + num)

def generate_graph(n, o_x, o_y, density):
  lines = []
  lines += ['\\begin{center}']
  lines += ['\\begin{tikzpicture}[scale=2]']

  for i in range(n):
    angle = (math.pi * 2 / n) * i
    c = to_char(i)
    x = o_x + math.cos(angle)
    y = o_y + math.sin(angle)
    lines += [f'\coordinate ({c}) at ({x:.5f},{y:.5f});']

  edges = rand(n, n, density=density)

  for i,j in zip(edges.row, edges.col):
    lines += [f'\draw[thick] ({to_char(i)}) -- ({to_char(j)});']

  for i in range(n):
    lines += [f'\draw[thick, fill=white] ({to_char(i)}) circle (0.1) node {{{to_char(i)}}};']

  lines += ['\\end{tikzpicture}']
  lines += ['\\end{center}']

  return [line+'\n' for line in lines]

n = 24
o_x = 1
o_y = 1
ritka = generate_graph(n,o_x,o_y,0.02)
suru = generate_graph(n,o_x,o_y,0.15)

with open('../01_motivacio/ritka_graf.tex', 'w') as f:
  f.writelines(ritka)

with open('../01_motivacio/suru_graf.tex', 'w') as f:
  f.writelines(suru)

