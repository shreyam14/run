from random import randint
def random_door():
       return randint(1, 3)
trial_count = 10000
stay_wins = 0
switch_wins = 0
for i in range(0,trial_count,1):
        prize_door = random_door()
        selected_door = random_door()
        opened_door = list(d for d in range(1, 4) if d != selected_door and d != prize_door)[0]
        switch_door = list(d for d in range(1, 4) if d != selected_door and d != opened_door)[0]
        if selected_door == prize_door:
                stay_wins += 1
        if switch_door == prize_door:
                switch_wins += 1


print("STAY :{} and SWITCH :{}".format(float(stay_wins) / float(trial_count),float(switch_wins) / float(trial_count)) )
