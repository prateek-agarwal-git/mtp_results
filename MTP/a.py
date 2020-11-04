#!/usr/bin/env python3
import random

x = 1
X = []
for i in range(100):
  X.append(x/32)
  x = 0.9 * x+ 0.1*random.randint(i%32,32)
print(X)
