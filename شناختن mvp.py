"""count=int(input("how many players? \n"))
result=[]
biggest=0
for i in range(count):
    player=str(input(f"enter a player {i+1} name?\n"))
    kill=int(input("how many kill we have?\n"))
    result.append((player,kill))
for player,kill in result:
    if kill<biggest:
        kill=biggest
        best_player=player
print(result)
print("MVP :",best_player)
print("biggest_kill:",biggest)"""
"""result = [
    ("Benyamin", 15),
    ("Reza", 21),
    ("Arman", 12),
    ("Ali", 18)]
total=0
winner=""
biggest=0
for player,kill in result:
    total+=kill
    if kill>biggest:
        kill=biggest
        winner=player
avrage=total/len(result)
print(winner,kill)
print(total)
print("avrage:",avrage)""""""
result = [
    ("Benyamin", 15),
    ("Reza", 21),
    ("Arman", 12),
    ("Ali", 18)
]

total = 0
winner =""
biggest = 0
loser=""
Least=90
for player, kill in result:
    total += kill

    if kill > biggest:
        biggest=kill
        winner = player
    elif Least > kill:
        Least=kill
        loser=player
average = total / len(result)
print("loser:",loser)
print("Least:",Least)
print("winner:",winner)
print("biggest:",biggest)
print("total:",total)
print("average:", average)
"""
"""برنامه‌ای بنویس که:
1. مجموع کیل‌های Team A را حساب کند.
2. میانگین Team A را حساب کند.
3. مجموع کیل‌های Team B را حساب کند.
4. میانگین Team B را حساب کند.
5. در آخر بگوید کدام تیم میانگین بیشتری دارد."""
team_a = [
    ("Benyamin", 15),
    ("Reza", 21),
    ("Arman", 12),
    ("Ali", 18)
]
team_b = [
    ("Sina", 20),
    ("Amir", 14),
    ("Mahan", 17),
    ("Pouya", 16)
]
total_a=0
total_b=0
biggest_a=0
biggest_b=0
winner_a=""
winner_b=""
for player ,kill in team_a:
    total_a+=kill
    avrage_a=total_a/len(team_a)
    if biggest_a<kill:
        biggest_a=kill
        winner_a=player
for player,kill in team_b:
    total_b+=kill
    avrage_b=total_b/len(team_b)
    if biggest_b<kill:
        biggest_b=kill
        winner_b=player

print("Team A's MVP ✅",winner_a,biggest_a)
print("Team B's MVP ✅",winner_b,biggest_b)
print("The avrage of Team A",avrage_a)
print("The avrage of Team B",avrage_b)
print("The total kill of Team A :",total_a)
print("The total kill of Team B",total_b)
if avrage_a>avrage_b:
    print("Team A wins! 🏆")
else:
    print("Team B wins! 🏆")
if biggest_a>biggest_b:
    print("MVP of this round 🏆",winner_a)
else:
    print("MVP of this round 🏆",winner_b)