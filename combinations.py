def combinations(string):
  if len(string) == 1:
    return ["", string]
  else:
    b = combinations(string[1:])
    return b + [string[0] + x for x in b]

print combinations("absdc")
