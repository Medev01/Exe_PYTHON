from collections import deque
D = deque()

D.append(20)
D.append(22)
D.appendleft(1)
D.extend([2,44,34])
D.extend([4])

print(D, type(D))