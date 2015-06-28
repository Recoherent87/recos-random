def win():
    print "You have defeated a",MONSTER,"!"
    GOLD = GOLD + MONGOLD
    return GOLD
def attack():
    MONHEALTH = MONHEALTH - (ATTACK - MONDEFENSE)
    print "The",MONSTER,"takes",str((ATTACK - MONDEFENSE)),"damage!"
    if MONHEALTH =< 0:
        win()
    else:
        return MONHEALTH
def defend():
    print "You defend!"
    DEFENSE = DEFENSE + 5
    return DEFENSE
def monattack():
    HEALTH = HEALTH - (MONATTACK - DEFENSE)
    print "You take",str((MONATTACK - DEFENSE)),"damage!"
    return HEALTH
