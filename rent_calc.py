###################
# Square footages #
###################
TOTAL_RENT = 8800
TOTAL_SQUARE_FOOTAGE = 1626 # $5.41 a square foot

daniel = ("daniel", (7 + 10/12)**2) # perfect closet space, fantastic light, roof deck, bay view
grady = ("grady", 13*(14 + 10/12)) # patio access, not great light, loud potentially
francis = ("francis", 11.5*9) # decent closet space, great light
kim_aziz = ("kim/aziz", 12.5**2) # great light, great closet space, bay view, shared
maya_dan_seb = ("maya/dan/seb", 21.5*17) # great light, slightly sub-decent closet space, bay view, sink, shared
kelly = ("kelly", 12.5**2) # ample closet space, great light, bay view
ari = ("ari", 11.5*9) # decent closet space, not much light, sink

rooms = [daniel, grady, francis, kim_aziz, maya_dan_seb, kelly, ari] 

def get_common_space():
    return TOTAL_SQUARE_FOOTAGE - sum([room[1] for room in rooms])

def get_prices():
    COMMON_SPACE = get_shared_space()
    for pair in zip([room[0] for room in rooms], map(lambda x: TOTAL_RENT * x[1] / (TOTAL_SQUARE_FOOTAGE - COMMON_SPACE), rooms)):
        print("{}: {}".format(pair[0], pair[1]))

def add_closet(n):
    for room in [daniel, kim_aziz, kelly, ari, francis]:
        room *= n

def add_natural_light(n):
    for room in [kim_aziz, maya_dan_seb, kelly]:
        room *= n

def reduce_shared(n):
    maya_dan_seb *= n/2
    kim_aziz *= n

if __name__ == "__main__":
    get_prices()