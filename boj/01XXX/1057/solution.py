from sys import stdin

N, Kim, Lim = map(int, stdin.readline().split())

round: int = 1
cur_round: list[int] = list(range(1, N + 1))
next_round: list[int] = []

game: bool = True
while game and len(cur_round) > 1:
    # 김지민과 임한수가 아니라면, 누가 이기던 풀이에 상관없으므로 무조건 왼쪽 사람이 이긴다고 가정하자.
    idx: int = 0
    participants: int = len(cur_round)
    while participants > 1:
        match cur_round[idx:idx + 2]:
            case [i, j] if i == Kim and j == Lim or i == Lim and j == Kim:
                print(round)
                game = False
                break
            case [i, j] if i == Kim or j == Kim:
                next_round.append(Kim)
            case [i, j] if i == Lim or j == Lim:
                next_round.append(Lim)
            case [i, _]:
                next_round.append(i)
        idx += 2
        participants -= 2
    if participants:
        # 부전승
        next_round.append(cur_round[-1])
        
    cur_round.clear()
    cur_round.extend(next_round)
    next_round.clear()
    round += 1
if game:
    print(-1)