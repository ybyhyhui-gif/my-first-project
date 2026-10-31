
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
