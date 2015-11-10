#The following program takes the input conditions as Name, Order,ExpectedAddress,WrongAddress, and evaluates these conditions for all permutations.
# 1.    The customer who ordered the Candelabrum received the Banister
# 2.    the customer who ordered the Banister received the package that Irene had ordered
# 3.    Frank received a Doorknob.
# 4.    George package went to KirkwoodStreet.
# 5.    KirkwoodStreet delivery was sent to LakeAvenue.
# 6.    Heather received the package that was to go to OrangeDrive
# 7.    Jerry received Heather order
# 8.    The Elephant arrived in North Avenue
# 9.    The person who had ordered Elephant received the package that should have gone to Maxwell Street.
# 10.    Maxwell Street received the Amplifier.
#Final Set of conditions derived:
# O[n.index('Irene')]!=RO[O.index('Banister')]
# O[n.index('George')]!=RO[EA.index('KirkwoodStreet')]
# RO[n.index('Jerry')]!=O[n.index('Heather')]
# EA.index('MaxwellStreet')!=RO.index('Amplifier')
# WA.index('NorthAvenue)!=RO.index('Elephant')
# EA.index('KirkwoodStreet')!=WA.index('LakeAvenue')
# n.index('George')!=WA.index('KirkwoodStreet')
# n.index('Frank')!=RO.index('Doorknob')
# O.index('Candelabrum')!=RO.index('Banister')
# O[EA.index('OrangeDrive')!=RO[n.index('Heather')]
# RO[O.index('Elephant')]!=O[EA.index('MaxwellStreet')]

#reference: 
#https://web.stanford.edu/~laurik/fsmbook/examples/Einstein'sPuzzle.html
# Start of program-
import itertools
from itertools import permutations
Name =['Frank','George','Heather','Irene','Jerry']
Order =['Amplifier','Banister','Candelabrum','Doorknob','Elephant']
ReceivedOrder =['Amplifier','Banister','Candelabrum','Doorknob','Elephant']
ExpectedAddress =['KirkwoodStreet','LakeAvenue','MaxwellStreet','NorthAvenue','OrangeDrive']
WrongAddress =['KirkwoodStreet','LakeAvenue','MaxwellStreet','NorthAvenue','OrangeDrive']

for n in itertools.permutations(Name):
    for RO in itertools.permutations(ReceivedOrder):
        for O in itertools.permutations(Order):
            if (n.index('Frank')!=RO.index('Doorknob')):
                continue
            for O in itertools.permutations(Order):
                if (O[n.index('Irene')]!=RO[O.index('Banister')] or RO[n.index('Jerry')]!=O[n.index('Heather')] or O.index('Candelabrum')!=RO.index('Banister')):
                    continue
                for EA in itertools.permutations(ExpectedAddress):
                    if (O[n.index('George')]!= RO[EA.index('KirkwoodStreet')] or O[EA.index('OrangeDrive')]!=RO[n.index('Heather')] or RO[O.index('Elephant')]!=O[EA.index('MaxwellStreet')] or EA.index('MaxwellStreet')!=RO.index('Amplifier')):
                        continue
                    for WA in itertools.permutations(WrongAddress):
                        if (WA.index('NorthAvenue')!=RO.index('Elephant') or EA.index('KirkwoodStreet')!=WA.index('LakeAvenue') or n.index('George')!=WA.index('KirkwoodStreet')):
                            continue
                     
                        print ("Frank Ordered-",O[n.index('Frank')],"and lives at- ",EA[n.index('Frank')])
                        print ("George Ordered-",O[n.index('George')],"and lives at- ",EA[n.index('George')])
                        print ("Heather Ordered-",O[n.index('Heather')],"and lives at- ",EA[n.index('Heather')])
                        print ("Irene Ordered-",O[n.index('Irene')],"and lives at- ",EA[n.index('Irene')])
                        print ("Jerry Ordered-",O[n.index('Jerry')],"and lives at- ",EA[n.index('Jerry')])
                        
                        break
                        break
                    break
                break
            break
        break
    

                

                               
                


                    
                
                        
                   
                        
            
