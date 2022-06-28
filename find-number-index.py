import math;
x = int(input(""));
tuple = (1, 2, 3, 4, 7, 7, 8, 9, 10);
origin = 0;
term = len(tuple - 1);
p = math.trunc((origin + term)/2);

while tuple[p] != x:
  if tuple[p] < x:
    origin = p;
  else:
    term = p;
  
  p = math.trunc((origin + term)/2);

  print(p, tuple[p]);
