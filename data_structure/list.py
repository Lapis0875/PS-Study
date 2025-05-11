class Node[T]:
    """단방향 연결 리스트의 노드 클래스"""
    value: T
    next: "Node[T] | None"

    def __init__(self, value, next=None):
        self.value = value
        self.next = next
    
    def __str__(self) -> str:
        return f"Node({self.value}, next={self.next})"

class List[T]:
    """단방향 연결 리스트"""
    head: Node[T]  # 연결 리스트의 제일 첫 노드의 포인터
    end: Node[T]   # 연결 리스트의 제일 마지막 노드의 포인터

    def __init__(self, value: T | None = None):
        self.head = Node[T](value) if value is not None else None
        self.end = None

    def append(self, value: T):
        """연결 리스트의 맨 끝에 새 노드를 추가한다."""
        if self.head is None:
            self.head = Node[T](value)
            self.end = self.head
        else:
            self.end.next = Node[T](value)
            self.end = self.end.next

    def delete(self, idx: int):
        """연결 리스트의 idx번째 노드를 삭제한다."""
        prev: Node[T] = self.head
        for i in range(1, idx-1):
            prev = prev.next

            # idx가 연결 리스트의 길이보다 크면 예외 발생
            if prev is None:
                raise IndexError("Index out of range")
        
        node = prev.next
        prev.next = node.next
        del node

    def insert(self, idx: int, value: T):
        """연결 리스트의 idx번째에 새 노드를 삽입한다."""
        node: Node[T] = self.head
        for i in range(1, idx):
            node = node.next

            # idx가 연결 리스트의 길이보다 크면 예외 발생
            if node is None:
                raise IndexError("Index out of range")
        
        next = node.next
        node.next = Node[T](value, next)
    
    def index(self, value: T) -> int:
        """연결 리스트에서 value의 인덱스를 반환한다. 없으면 -1을 반환한다."""
        node: Node[T] = self.head
        idx = 0
        while node is not None:
            if node.value == value:
                return idx
            node = node.next
            idx += 1
        return -1

    def length(self) -> int:
        """연결 리스트의 길이를 반환한다."""
        node: Node[T] = self.head
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count
    
    def __iter__(self):
        """연결 리스트를 순회할 수 있도록 해준다."""
        node: Node[T] = self.head
        while node is not None:
            yield node.value
            node = node.next

single_list = List[int]()

for i in range(1, 11):
    single_list.append(i)

for n in single_list:
    print(n, end=" ")
print()

idx = single_list.index(5) # 값이 5인 노드의 인덱스 탐색
print(idx)
single_list.delete(idx)

for n in single_list:
    print(n, end=" ")
print()

print(single_list.length()) # 연결 리스트의 길이 탐색