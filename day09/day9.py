lines: list[str] = []
with open("day9.txt", "r") as file:
    lines = file.read().splitlines()

def parseMoves(lines):
    moves = []
    for line in lines:
        count = int(line[2:])
        for step in range(count):
            match line[0]:
                case "U":
                    moves.append((0, 1))
                case "D":
                    moves.append((0, -1))
                case "R":
                    moves.append((1, 0))
                case "L":
                    moves.append((-1, 0))
    return moves

def distance(new, old):
    x = abs(new[0] - old[0])
    y = abs(new[1] - old[1])
    return max(x, y)

moves = parseMoves(lines)

# A -> B -> C -> D
# move A, drag b

class Tail:
    def __init__(self, pos, next) -> None:
        self.pos = pos
        self.next = next

# def drag(head, tail: Tail) -> tuple[int, int]:
    
def makeMoves(length):
    solution = {}
    head = (0, 0)
    tail = Tail((0, 0), None)
    for move in moves:
        old = head
        head = (head[0] + move[0], head[1] + move[1])
        if distance(head, tail.pos) > 1:
            tail.pos = old

        solution[tail.pos] = solution.get(tail.pos, 0) + 1
    return solution

print(len(makeMoves(1)))
