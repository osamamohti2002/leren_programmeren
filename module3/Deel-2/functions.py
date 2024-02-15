import time
from termcolor import colored
from math import ceil
from data import JOURNEY_IN_DAYS, mainCharacter,COST_FOOD_HORSE_COPPER_PER_DAY, COST_FOOD_HUMAN_COPPER_PER_DAY, COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK

##################### O03 #####################

def copper2silver(amount:int) -> float:
    aantal_silver = amount * 0.1
    return aantal_silver


def silver2gold(amount:int) -> float:
    aantal_goud = amount * 0.2
    return aantal_goud

def copper2gold(amount:int) -> float:
    copper_to_gold = amount * 0.02
    return copper_to_gold

def platinum2gold(amount:int) -> float:
    platinum_to_gold = amount * 25
    return platinum_to_gold


def getPersonCashInGold(personCash:dict) -> float:
    total_gold = 0
    
    total_gold += copper2gold(personCash.get('copper', 0))
    
    total_gold += silver2gold(personCash.get('silver', 0))
    
    total_gold += personCash.get('gold', 0)
    
    total_gold += platinum2gold(personCash.get('platinum', 0))
    
    return total_gold


##################### O05 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    total_cost_copper = (people * COST_FOOD_HUMAN_COPPER_PER_DAY + horses * COST_FOOD_HORSE_COPPER_PER_DAY) * JOURNEY_IN_DAYS
 
    total_cost_gold = total_cost_copper / 100 * 2 
    return total_cost_gold
    
##################### O06 #####################

def getFromListByKeyIs(lst: list, key: str, value: any) -> list:
    filtered_list = []
    for item in lst:
        if item.get(key) == value:
            filtered_list.append(item)
    return filtered_list
 
def getAdventuringPeople(people: list) -> list:
    adventuring_people = []
    for person in people:
        if person.get('adventuring') == True:
            adventuring_people.append(person)
    return adventuring_people
 
def getShareWithFriends(friends: list) -> list:
    share_with_friends = []
    for friend in friends:
        if friend.get('shareWith') == True:
            share_with_friends.append(friend)
    return share_with_friends
 
def getAdventuringFriends(friends: list) -> list:
    adventuring_friends = []
    adventuring_people = getAdventuringPeople(friends)
    share_with_friends = getShareWithFriends(friends)
    for friend in adventuring_people:
        if friend in share_with_friends:
            adventuring_friends.append(friend)
    return adventuring_friends

##################### O07 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
    total_cost_horse = (horses * COST_HORSE_SILVER_PER_DAY / 5) * JOURNEY_IN_DAYS
   
   
    total_cost_tent = (tents * COST_TENT_GOLD_PER_WEEK ) * ceil(JOURNEY_IN_DAYS/7)
 
    total_cost = total_cost_horse + total_cost_tent
    return total_cost
##################### O08 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### O09 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### O10 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### O11 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### O13 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### O14 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################

def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()




