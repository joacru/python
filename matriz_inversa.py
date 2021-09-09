def init_matriz(m, n):
  ret = [[0 for i in range(n)] for j in range(m)]
  return ret

def cargar_matriz():
  m = int(input('Ingresa la cantidad de filas y columnas: '))
  n = m
  ret = init_matriz(m, n)
  for i in range(m):
    fila = input(f'Ingresa los valores de la {i + 1}° fila separados por un espacio: ').split(' ')
    for j in range(n):
      ret[i][j] = int(fila[j])
  return ret

def obtener_mn(matrix):
  m = len(matrix)
  n = len(matrix[0])
  return (m, n)

def multiplicar_matriz_constante(matrix, k):
  m, n = obtener_mn(matrix)
  ret = [[matrix[i][j] * k for j in range(n)] for i in range(m)]
  return ret

def transponer(matrix):
  m, n = obtener_mn(matrix)
  trans = init_matriz(n, m)
  for i in range(m):
    for j in range(n):
      trans[j][i] = matrix[i][j]
  return trans

def determinante(matrix):
  m, n = obtener_mn(matrix)
  if m == 1 and n == 1:
    return matrix[0][0]
  elif m == 2 and n == 2:
    return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
  ret = 0
  for i in range(m):
    p = 1
    q = 1
    for j in range(n):
      a = (i + j) % m
      b = j
      p *= matrix[a][b]
      b = n - j - 1
      q *= matrix[a][b]
    ret += p - q
  return ret

def eliminar_fc(matrix, f, c):
  m, n = obtener_mn(matrix)
  ret = []
  for i in range(m):
    if i == f:
      continue
    ret.append([])
    for j in range(n):
      if j == c:
        continue
      ret[-1].append(matrix[i][j])
  return ret

def matriz_adjunta(matrix):
  m, n = obtener_mn(matrix)
  ret = init_matriz(m, n)
  for i in range(m):
    for j in range(n):
      ret[i][j] = (-1)**(i + j) * determinante(eliminar_fc(matrix, i, j))
  return ret

def matriz_inversa(matrix):
  adjt = transponer(matriz_adjunta(matrix))
  ret = multiplicar_matriz_constante(adjt, 1 / determinante(matrix))
  return ret

def run():
  try:
    matrix = cargar_matriz()
  except:
    print('Los datos ingresados son incorrectos o tienen un formato equivocado.')
    return
  inversa = matriz_inversa(matrix)
  print(inversa)

if __name__ == '__main__':
  run()