import sys
    
def print100(a):
  try:
    b = 1/(101-a)
  except ZeroDivisionError:
    sys.exit()
  print a
  print100(a+1)

print100(1)
