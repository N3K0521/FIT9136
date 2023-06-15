# Date: Mar 22nd 2023
# Name: Huixin Wang
'''Description:
    Update the value for “Phelps” in the dictionary swimmers to include his  
    medals from the Rio Olympics by adding 5 to the current value (Phelps will 
    now have 28 total medals). Do not rewrite the dictionary.
'''
 
# create the dictionary where the key are the name of swimmers and values are their number of medals 
swimmers = {'Manuel':4, 'Lochte':12, 'Adrian':7, 'Ledecky':5, 'Dirado':4, 'Phelps':23}
swimmers["Phelps"] += 5
print(swimmers)
