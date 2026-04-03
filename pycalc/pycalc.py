def add(a, b):
  res = a
  if b > 0:
    while (b - 1) >= 0:
      b -= 1
      res += 1
  elif b < 0:
    while (b + 1) <= 0:
      b += 1
      res -= 1
  return res

def subtract(a, b):
  res = a
  if b > 0:
    while (b - 1) >= 0:
      b -= 1
      res -= 1
  elif b < 0:
    while (b + 1) <= 0:
      b += 1
      res += 1
  return res

def multiply(a, b):
  res = a
  c = abs(b)
  if c == 0:
    return 0
  elif c > 0:
    while (c - 1) > 0:
      c -= 1
      res += a
  
  if b > 0:
    return res
  elif b < 0:
    return -res
  
def divide(a, b):
  return a / b
