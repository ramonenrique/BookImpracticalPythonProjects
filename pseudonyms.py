#Thsi is first file in this project.
import sys,random
print("Welcome to the Psych 'Sidekick Name Picker'\n")
print("A name just like Sean would pick for Gus\n\n")


first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill 'BeenieWeenie'","Bob 'Stinkbug'", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
'Chewy', 'Chigger", "Cinnabuns', 'Cleet', 'Cornbread', 'Crab Meat','Crapps', 'Dark Skies', 'Dennis Clawhammer', 'Dicman', 'Elphonso',
'Fancypants', 'Figgs', 'Foncy', 'Gootsy', 'Greasy Jim', 'Huckleberry','Huggy', 'Ignatious', 'Jimbo', "Joe 'Pottin Soil'", 'Johnny',
'Lemongrass', 'Lil Debil', 'Longbranch', '"Lunch Money"','Mergatroid', '"Mr Peabody"', 'OilCan','Oinks', 'Old Scratch','Ovaltine', 'Pennywhistle', 'Pitchfork Ben', 'Potato Bug',
'Pushmeet','Rock Candy', 'Schlomo', 'Scratchensniff', 'Scut',"Sid 'The Squirts'", 'Skidmark', 'Slaps', 'Snakes', 'Snoobs',
'Snorki', 'Soupcan Sam', 'Spitzitout', 'Squids', 'Stinky','Storyboard', 'Sweet Tea', 'TeeTee', 'Wheezy Joe',"Winston 'Jazz Hands'", 'Worms')


last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple', 'Goodensmith',
'Goodpasture', 'Guster', 'Henderson', 'Hooperbag', 'Hoosenater',
'Hootkins', 'Jefferson', 'Jenkins', 'JingleySchmidt',
'Johnson',
'Kingfish', 'Listenbee', "M'Bembo", 'McFadden', 'Moonshine', 'Nettles',
'Noseworthy', 'Olivetti', 'Outerbridge', 'Overpeck', 'Overturf',
'Oxhandler', 'Pealike', 'Pennywhistle', 'Peterson', 'Pieplow',
'Pinkerton', 'Porkins', 'Putney', 'Quakenbush', 'Rainwater',
'Rosenthal', 'Rubbins', 'Sackrider', 'Snuggleshine', 'Splern',
'Stevens', 'Stroganoff', 'SugarGold',
'Swackhamer', 'Tippins',
'Turnipseed', 'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax',
'Weiners', 'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
'Woolysocks')

vattempts=0

while True:
    vFirstName=random.choice(first)
    vLastName=random.choice(last)
    vattempts+=1
    print('\n')
    print("{}:{} {}".format(vattempts,vFirstName,vLastName),file=sys.stderr)

    vask_try_again=input("\n\n Do you want to try again? (Enter)= Try again (q)=quit \n")
    if vask_try_again.lower()=='q':
        break

print("Bye, thanks for playing")

quit()

