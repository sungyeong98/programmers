from collections import defaultdict
def solution(n, results):
    winner = defaultdict(set)
    loser = defaultdict(set)
    
    for a, b in results:
        winner[a].add(b)
        loser[b].add(a)
    
    for player in range(1, n+1):
        for win_player in loser[player]:
            winner[win_player].update(winner[player])
        for lose_player in winner[player]:
            loser[lose_player].update(loser[player])
    
    return sum([1 if len(winner[i]) + len(loser[i]) == n-1 else 0 for i in range(1, n+1)])