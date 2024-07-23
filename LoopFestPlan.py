# Utilize for loops to iterate over multiple lists and organize event details without using functions.

events = ["BBQ", "family reunion", "birthday party", "Thanksgiving dinner", "New Years Eve party"]
music = ["disco", "throwbacks", "hip-hop", "Bad Bunny"]

for event in events:
    for genre in music:
        print("For a " + event +  ", play some " + genre + "!")
