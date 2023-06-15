# Date: Mar 22nd 2023
# Name: Huixin Wang
'''Description:
    We have a dictionary of the specific events that Italy has won medals in and  
    the number of medals they have won for each event. Assign to the variable 
    events a list of the keys from the dictionary medal_events. Do not hard code this.
'''
 
# create the dictionary where the key are the specific events and values are the number of medals Italy have won for each event
medal_events = {'Shooting': 7, 'Fencing': 4, 'Judo': 2, 'Swimming': 3, 'Diving': 2}

events = (list(medal_events.keys()))
print(events)
