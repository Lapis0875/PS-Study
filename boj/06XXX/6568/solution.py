input = open(0).readline

CodeTypes = {
    "000": "sta",
    "001": "lda",
    "010": "beq",
    "011": "nop",
    "100": "dec",
    "101": "inc",
    "110": "jmp",
    "111": "hlt",   # PC값을 32로 바꾸는 방식으로는 종료시킬 수 없다.
}

# 메모리 주소값은 2진수 정수값 문자열로 인식하고 파싱한다.
class Code:
    c_type: str     # 3자리 명령어 유형 값
    address: int    # 5자리 메모리 주소값
    __slots__ = ("c_type", "address")

    def __init__(self, c_type: str, address: int):
        self.c_type = c_type
        self.address = address

    @classmethod
    def parse(cls, bytecode: str) -> "Code":
        """Parse a single line of byte code."""
        return cls(CodeTypes[bytecode[:3]], int(bytecode[3:], 2))

class Interpreter:
    pc: int = 0
    acc: int = 0
    memory: list[str] = ["" for _ in range(32)]

    def init(self):
        """실행 환경 초기화"""
        for i in range(32):
            self.memory[i] = input().rstrip()
            # 로컬에서 테스트 케이스 돌릴 때 빈 문자열이 들어와서 예외처리해둠.
            if self.memory[i] == '':
                raise EOFError()
        self.pc = 0
        self.acc = 0

    # Code Functions
    def sta(self, x: int) -> bool:
        """STA x: 메모리의 x번째 주소에 현재 가산기 값을 저장한다.
        @param x: 5bit짜리 메모리 주소값.
        """
        self.memory[x] = format(self.acc, "08b")
        return False
    
    def lda(self, x: int):
        """LDA x: 메모리의 x번째 주소에 있는 값을 현재 가산기로 불러온다.
        @param x: 5bit짜리 메모리 주소값.
        """
        self.acc = int(self.memory[x], 2)
        return False
  
    def beq(self, x: int):
        """BEQ x: 현재 가산기의 값이 0이라면, PC를 x로 바꾼다.
        @param x: 5bit짜리 메모리 주소값.
        """
        if self.acc == 0:
            self.pc = x
        return False
    
    def nop(self, x: int):
        """NOP -: 아무 연산도 하지 않는다.
        @param x: 5bit짜리 메모리 주소값. (사용되지 않는다.)
        """
        return False
    
    def dec(self, x: int):
        """DEC -: 가산기 값을 1 감소시킨다.
        @param x: 5bit짜리 메모리 주소값. (사용되지 않는다.)
        """
        self.acc -= 1
        if self.acc < 0:
            self.acc = 255
        return False
    
    def inc(self, x: int):
        """INC -: 가산기 값을 1 증가시킨다.
        @param x: 5bit짜리 메모리 주소값. (사용되지 않는다.)
        """
        self.acc += 1
        if self.acc > 255:
            self.acc = 0
        return False
    
    def jmp(self, x: int):
        """JMP x: PC 값을 x로 바꾼다.
        @param x: 5bit짜리 메모리 주소값.
        """
        self.pc = x
        return False
    
    def hlt(self, x: int):
        """HLT -: 프로그램을 종료한다.
        @param x: 5bit짜리 메모리 주소값. (사용되지 않는다.)
        """
        return True

    def run(self):
        while True:
            c = Code.parse(self.memory[self.pc])
            self.pc = self.pc + 1 if self.pc < 31 else 0
            halt = getattr(self, c.c_type)(c.address)
            if halt:
                break
        print(format(self.acc, "08b"))   # pc는 언제나 음이 아닌 정수

    
interpreter = Interpreter()
while True:
    try:
        interpreter.init()
        interpreter.run()
    except EOFError:
        break
