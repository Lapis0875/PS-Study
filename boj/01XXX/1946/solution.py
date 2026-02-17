import io, os

def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    output = ""
    for _ in range(int(input())):
        N = int(input())
        
        # 1. 서류 심사 순위를 기준으로 정렬한다.
        # 어차피 서류 순위가 곧 정렬된 결과의 인덱스이므로 굳이 정렬하지 않고 고정 길이의 배열을 활용하면 더 빠르다.
        # 또한, 이후 과정에서 서류 순위 값은 필요하지 않으므로 면접 순위 값만 저장한다.
        ranks = [0] * N
        for _ in range(N):
            a, b = map(int, input().split())
            ranks[a - 1] = b
        
        # 2. 서류 1등부터 내려가면서, 면접 순위를 비교해본다. 서류 1등의 면접 순위를 기준으로 더 높은 순위만 포함한다.
        min_rank = 100001 # 최대 순위는 100,000등
        cnt = 0
        for r in ranks:
            if r < min_rank:
                cnt += 1
                min_rank = r
                if min_rank == 1: # 더 이상 탐색할 필요 없음
                    break
        output += f"{cnt}\n"
    print(output)

main()