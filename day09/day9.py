def readLines(filename):
    with open(filename, "r") as file:
        return file.read().splitlines()

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
    def __init__(self, pos) -> None:
        self.pos = pos

    def distance(self, toPos):
        x = abs(toPos[0] - self.pos[0])
        y = abs(toPos[1] - self.pos[1])
        return max(x, y)

    def follow(self, toPos) -> tuple[int, int]:
        if self.distance(toPos) > 1:
            cmp = lambda a, b: (a > b) - (a < b)
            x = cmp(toPos[0], self.pos[0])
            y = cmp(toPos[1], self.pos[1])
            self.pos = (self.pos[0] + x, self.pos[1] + y)
        return self.pos

def play(moves, tailLength = 1):
    knots = []
    for _ in range(tailLength):
        knots.append(Knot((0, 0)))

    solution = {}
    headPos = (0, 0)
    for move in moves:
        headPos = (headPos[0] + move[0], headPos[1] + move[1])
        toPos = headPos
        for tailKnot in knots:
            toPos = tailKnot.follow(toPos)
        solution[toPos] = solution.get(toPos, 0) + 1
    return len(solution)

moves = parseMoves(readLines("day9example.txt"))
print("P1 E1", play(moves))
moves = parseMoves(readLines("day9.txt"))
print("P1", play(moves))

moves = parseMoves(readLines("day9example.txt"))
print("P2 E1", play(moves, 10))
moves = parseMoves(readLines("day9example2.txt"))
print("P2 E2", play(moves, 9))
moves = parseMoves(readLines("day9.txt"))
print("P2", play(moves, 9))
