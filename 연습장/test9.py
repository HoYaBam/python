list_a = [1,2,3,4,5,6,7,8,9]
for i in list_a:
    print(i)

import time

#5초동안 반복
target_tick = time.time() + 5
while time.time() < target_tick:
    print('메롱!!!!')

