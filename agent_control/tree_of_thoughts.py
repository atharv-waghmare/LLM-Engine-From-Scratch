class ToyPuzzle:
    def __init__(self, target=25):
        self.target = target

    def get_successors(self, state):
        return [] if state >= self.target else [state + 1, state * 2, state * 3]

    def is_goal(self, state):
        return state == self.target

    def score(self, state):
        return -9999 if state > self.target else -abs(self.target - state)

def dfs_tot(puzzle, state, max_depth, stats):
    stats['nodes_expanded'] += 1
    if puzzle.is_goal(state): return [state]
    if max_depth == 0: return None

    for nxt in puzzle.get_successors(state):
        path = dfs_tot(puzzle, nxt, max_depth - 1, stats)
        if path: return [state] + path
    return None

def bfs_beam_tot(puzzle, start, beam_width, max_depth, stats):
    frontier = [[start]]
    for depth in range(max_depth + 1):
        if not frontier:
            break

        nxt_frontier, seen = [], set()
        for path in frontier:
            curr = path[-1]
            stats['nodes_expanded'] += 1
            if puzzle.is_goal(curr):
                return path
            if depth == max_depth:
                continue
            for n in puzzle.get_successors(curr):
                if n not in seen:
                    seen.add(n)
                    nxt_frontier.append(path + [n])

        nxt_frontier.sort(key=lambda p: puzzle.score(p[-1]), reverse=True)
        frontier = nxt_frontier[:beam_width]

    return None