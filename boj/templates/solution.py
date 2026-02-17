import io, os

def main():
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline # 빠른 입출력. 하지만 CPH Judge에서 돌아가지 않음에 유의할 것.
    # input = open(0).readline # CPH Judge에서 결과 보려면 일단 이거로 바꾸고 써보자

main()