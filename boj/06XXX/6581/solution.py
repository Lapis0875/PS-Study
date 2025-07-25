from sys import stdin

html: list[str] = list(stdin.read())
line_length: int = 0
line_words: list[str] = []
buffer: list[str] = []
prev: str = ""

def push_line():
    global line_length
    print(" ".join(line_words))
    line_words.clear()
    line_length = 0

while html:
    c: str = html.pop(0)
    match c:
        case "<":   # handle new tag
            while (c := html.pop(0)) != ">":
                buffer.append(c)
            tag: str = "".join(buffer)
            match tag:
                case "br":
                    if line_length > 0:
                        push_line()
                    else:
                        print()
                    line_length = 0
                case "hr":
                    if line_length > 0:
                        push_line()
                    print("-" * 80)
                    line_length = 0
            prev = "\n"                 # 끝에 개행하므로 개행문자와 동일하게 처리한다.
            buffer.clear()
        case " " | "\n":
            if len(buffer) == 0:
                continue
            if prev == c:
                continue                        # 공백문자 또는 개행문자를 두 번 이상 처리하지 않는다.
            
            word_len: int = len(buffer)
            # print(">>>", "".join(buffer), f"line_len = {line_length}, word_len = {word_len}")
            if line_length + word_len > 80:                # 80자가 넘어갈 경우 새 줄을 시작한다.
                push_line()
                line_length = word_len
                line_words.append("".join(buffer))
            else:
                line_length += word_len + 1                 # 띄어쓰기
                line_words.append("".join(buffer))
            buffer.clear()
            prev = c
        case _:     # any char in word
            buffer.append(c)
            prev = c

if len(line_words):    
    word_len: int = len(buffer)
    # print(">>>", "".join(buffer), f"line_len = {line_length}, word_len = {word_len}")
    if line_length + word_len > 80:                # 80자가 넘어갈 경우 새 줄을 시작한다.
        push_line()
        print("".join(buffer))
    else:
        line_length += word_len + 1                 # 띄어쓰기
        line_words.append("".join(buffer))
        push_line()
       