from sys import stdin

A = int(stdin.readline().strip())   # 원래의 고기의 온도 A가 주어진다. 단, A는 -100 이상 100 이하이며, 0이 아니다.
B = int(stdin.readline().strip())   # 목표 온도 B가 주어진다. 단, B는 1 이상 100 이하이며, A보다 크다.
C = int(stdin.readline().strip())   # 얼어 있는 고기를 1℃ 데우는 데 걸리는 시간 C가 주어진다.
D = int(stdin.readline().strip())   # 얼어 있는 고기를 해동하는 데 걸리는 시간 D가 주어진다.
E = int(stdin.readline().strip())   # 얼어 있지 않은 고기를 1℃ 데우는 데 걸리는 시간 E가 주어진다.

"""
JOI 군은 가열할 때 고기가 아래의 규칙을 따라 데워진다고 가정하고, 고기를 데우는 데 걸리는 시간을 어림하기로 했다.

- 고기가 얼어 있고 온도가 0℃ 미만일 때 : 온도가 C초에 1℃씩 오른다.
- 고기가 얼어 있고 온도가 정확히 0℃일 때 : 얼어 있지 않은 상태로 만드는(해동하는) 데 D초가 걸린다.
- 고기가 얼어 있지 않을 때 : 온도가 E초에 1℃씩 오른다.

이 규칙을 토대로, 고기가 B℃까지 데워지는 데 몇 초가 걸리는지 구하라.
"""

if A < 0:   # 고기가 얼어 있는 상태
    if B < 0:   # 목표 온도가 0℃ 미만인 경우 -> 그냥 얼어있는채로 데우기만 하면 된다.
        print((B - A) * C)
    elif B == 0:   # 목표 온도가 0℃인 경우 -> 얼어있는 고기를 |A| * C초 데우고, 이후 D초 해동
        print(-A * C + D)
    else:   # 목표 온도가 0℃ 이상인 경우 -> 얼어있는 고기를 |A| * C초 데우고, D초 해동 후, 0℃에서 B℃까지 E초에 1℃씩 데우기
        print(-A * C + D + B * E)
else:       # 고기는 얼어 있지 않으며, 목표 온도 또한 0도보다 높다.
    print((B - A) * E)
