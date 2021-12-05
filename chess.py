import itertools
players = ['White','Black'] #taking turns.
turn = itertools.cycle(players)
countdown = itertools.count(10,-1)
print([turn for turn in itertools.takewhile(lambda x: next(countdown)>0,turn)])

#Building chess
name = ['Shreya','Rani','Amrit','Vasma','Ranvir']
fixture = [f"{p1} vs. {p2}"for p1 in name for p2 in name if p1!=p2]
print(fixture)
