s = input().strip()          # read input string
numbers = s.split("+")       # split into list, e.g. "3+2+1" -> ["3","2","1"]
numbers.sort()               # sort list as strings (works fine since only "1","2","3")
result = "+".join(numbers)   # join back with "+"
print(result)

