def points(games):
    points = 0
    for game in games: 
        if game[0] > game[2]:
            points += 3
        elif game[0] == game[2]:
            points += 1
        else: 
            continue
    
    return points

print(points(['1:0','2:0','3:0','4:0','2:1','3:1','4:1','3:2','4:2','4:3']))