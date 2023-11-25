from sys import stdin
from typing import Final, Literal, cast

type Operator = Literal["+", "-"]
Expression: Final[str] = stdin.readline().strip()

parsed_expression: list[int | Operator] = []
operator_pos: dict[Operator, list[int]] = {"+": [], "-": []}

buffer: list[str] = []
index: int = 0
for c in Expression:
    if c in "+-":
        parsed_expression.append(int("".join(buffer)))
        index += 1
        buffer.clear()
        parsed_expression.append(cast(Operator, c))
        operator_pos[cast(Operator, c)].append(index)
        index += 1
    else:
        buffer.append(c)
if buffer:
    parsed_expression.append(int("".join(buffer)))

# print(parsed_expression)
# print(operator_pos)

pos_sum: int = 0
if operator_pos["-"]:
    add_range: slice = slice(operator_pos["-"][0])
else:
    add_range: slice = slice(len(parsed_expression))
for num_or_op in parsed_expression[add_range]:
    if isinstance(num_or_op, int):
        pos_sum += num_or_op
    # 이 사이에 있는 연산자는 모두 +이므로, 굳이 처리할 필요 없다.

neg_len = len(operator_pos["-"])
neg_sum: list[int] = []
for neg_pos in range(neg_len):
    cur_sum: int = 0
    if neg_pos < neg_len - 1:
        add_range: slice = slice(operator_pos["-"][neg_pos] + 1, operator_pos["-"][neg_pos + 1])
    else:
        add_range: slice = slice(operator_pos["-"][neg_pos] + 1, len(parsed_expression))
    # print(add_range)
    for num_or_op in parsed_expression[add_range]:
        # print(num_or_op)
        if isinstance(num_or_op, int):
            cur_sum += num_or_op
        # 이 사이에 있는 연산자는 모두 +이므로, 굳이 처리할 필요 없다.
    neg_sum.append(-cur_sum)

# print(pos_sum, neg_sum)
total_neg = sum(neg_sum)

print(pos_sum + total_neg)
