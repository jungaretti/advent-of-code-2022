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

class Knot:
    def __init__(self, pos, tail = None) -> None:
        self.pos = pos
        self.tail = tail

    def distance(self, toPos):
        x = abs(toPos[0] - self.pos[0])
        y = abs(toPos[1] - self.pos[1])
        return max(x, y)

    def drag(self, fromPos, toPos) -> tuple[int, int]:
        old = self.pos
        if self.distance(toPos) > 1:
            self.pos = fromPos

def play(moves, length = 1):
    head = Knot((0, 0))
    last = head
    for _ in range(length):
        last.tail = Knot(last.pos)
        last = last.tail

    solution = {}
    for move in moves:
        old = head.pos
        head.pos = (head.pos[0] + move[0], head.pos[1] + move[1])
        head.tail.drag(old, head.pos)
        solution[head.tail.pos] = solution.get(head.tail.pos, 0) + 1
    
    return len(solution)

moves = parseMoves(lines)
print(play(moves))
