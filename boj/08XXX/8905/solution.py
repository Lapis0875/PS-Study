input = open(0).readline

K = 0 # 1 ~ 3 사이의 정수. 한 글자가 최대 몇 글자의 리트로 표현될 수 있는지를 정의한다.
text = ""
leet = ""
leet_map = {} # 각 알파벳 소문자의 리트 표기를 저장하는 맵.

def backtrack(text_idx, leet_idx):
    # 종료 조건
    if text_idx >= len(text): # text를 끝까지 탐색했을 때
        return leet_idx == len(leet) # leet 문자열이 아직 다 사용되지 않았다면 잘못된 경우이다.
    elif leet_idx >= len(leet): # text는 남아있는데 leet 문자열이 다 사용됬다면 잘못된 경우이다.
        return False

    text_char = text[text_idx]
    # 리트 표기에서, 한 가지 알파벳은 하나의 리트 표기로만 변환된다.
    # 따라서, 앞서 변환한 적이 있는 문자라면 이번 문자도 동일한 리트 표기로 변환해보고, 불가능하다면 즉시 False로 반환하고 종료한다.
    # 서로 다른 두 문자가 같은 리트 표기로 변환될 수 있다.
    # 리트 표기는 기존 알파벳과 비슷해 보이지 않아도 된다
    if leet_map.get(text_char, None) is not None:
        for d in range(len(leet_map[text_char])):
            try:
                if leet[leet_idx + d] != leet_map[text_char][d]:
                    return False
            except IndexError:
                return False
        # 기존 리트 표기로 변형 가능하다면, 이후 문자부터 계속 탐색한다.
        return backtrack(text_idx + 1, leet_idx + len(leet_map[text_char]))
    else:
        # 기존에 리트 표기로 변환한 적 없는 새로운 문자라면, 1 ~ K까지의 길이로 리트 문자열을 읽어들여 리트 표기로 사용하고 이후 문자의 탐색을 진행해본다.
        for d in range(1, K + 1):
            if leet_idx + d > len(leet):
                break
            leet_map[text[text_idx]] = leet[leet_idx:leet_idx+d]
            res = backtrack(text_idx + 1, leet_idx + d)
            if res:
                return True
        
        # 다음 백트래킹을 위해 이번 분기의 탐색 정보 정리하기
        del leet_map[text[text_idx]]
        return False

for _ in range(int(input())):
    K = int(input())
    text = input().strip()
    leet = input().strip()
    leet_map.clear()
    
    print("1" if backtrack(0, 0) else "0")
