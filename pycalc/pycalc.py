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
  return a * b
  
def divide(a, b):
  return a / b
