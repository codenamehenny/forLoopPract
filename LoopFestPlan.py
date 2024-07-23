# Utilize for loops to iterate over multiple lists and organize event details without using functions.

# 2 lists for event type and music type
events = ["BBQ", "family reunion", "birthday party", "Thanksgiving dinner", "New Years Eve party"]
music = ["disco", "throwbacks", "hip-hop", "Bad Bunny"]

# nested for loop with combination between the 2 lists
for event in events:
    for genre in music:
        print("For a " + event +  ", play some " + genre + "!")
