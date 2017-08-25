###################
# Square footages #
###################
TOTAL_RENT = 8800
TOTAL_SQUARE_FOOTAGE = 1626 # $5.41 a square foot

daniel = (7 + 10/12)**2 # perfect closet space, fantastic light, roof deck, bay view
grady = 13*(14 + 10/12) # patio access, not great light, loud potentially
francis = 11.5*9 # decent closet space, great light
kim_aziz = 12.5**2
maya_dan_seb = 21.5*17 # great light, slightly sub-decent closet space, bay view, sink, shared
kelley = 12.5**2 # ample closet space, great light, bay view
ari = 11.5*9 # decent closet space, not much light, sink

rooms = [daniel, grady, francis, kim_aziz, maya_dan_seb, kelley, ari] 

def get_shared_space():
    return TOTAL_SQUARE_FOOTAGE - sum(rooms)

def add_closet(n):
    for room in [daniel, kim_aziz, kelley, ari, francis]:
        room *= n

def add_natural_light(n):
    for room in [kim_aziz, maya_dan_seb, kelley]:
        room *= n

def reduce_shared(n):
    maya_dan_seb *= n/2
    kim_aziz *= n
