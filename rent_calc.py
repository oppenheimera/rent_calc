###################
# Square footages #
###################
TOTAL_RENT = 8800
TOTAL_SQUARE_FOOTAGE = 1626 # $5.41 a square foot
ALPHA = 1.5

daniel = ["daniel", (7 + 10/12)**2] # perfect closet space, fantastic light, roof deck, bay view
grady = ["grady", 13*(14 + 10/12)] # patio access, not great light, loud potentially
francis = ["francis", 11.5*9] # decent closet space, great light
kim_aziz = ["kim/aziz", 12.5**2] # great light, great closet space, bay view, shared
maya_dan_seb = ["maya/dan/seb", 21.5*17] # great light, slightly sub-decent closet space, bay view, sink, shared
kelly = ["kelly", 12.5**2] # ample closet space, great light, bay view
ari = ["ari", 11.5*9] # decent closet space, not much light, sink

rooms = [daniel, grady, francis, kim_aziz, maya_dan_seb, kelly, ari] 

def get_common_space():
    return TOTAL_SQUARE_FOOTAGE - sum([room[1] for room in rooms])

def get_prices():
    COMMON_SPACE = get_common_space()
    s = 0
    for pair in zip([room[0] for room in rooms], map(lambda x: TOTAL_RENT * (x[1] / (TOTAL_SQUARE_FOOTAGE - COMMON_SPACE)), rooms)):
        s += pair[1]
        print("{}: {}".format(pair[0], pair[1]))
    print("total: {}".format(s))

def add_closet():
    daniel[1] *= 7/10 * ALPHA
    grady[1] *= 3.5/10 * ALPHA
    francis[1] *= 6/10 * ALPHA
    kim_aziz[1] *= 5/10 * ALPHA
    maya_dan_seb[1] *= 4/10 * ALPHA
    kelly[1] *= 9/10 * ALPHA
    ari[1] *= 7/10 * ALPHA
 
def add_natural_light():
    daniel[1] *= 10/10 * ALPHA
    grady[1] *= 4/10 * ALPHA
    francis[1] *= 7/10 * ALPHA
    kim_aziz[1] *= 10/10 * ALPHA
    maya_dan_seb[1] *= 10/10 * ALPHA
    kelly[1] *= 10/10 * ALPHA
    ari[1] *= 3/10 * ALPHA

def reduce_shared():
    kim_aziz[1] *=  5/10 * ALPHA
    maya_dan_seb[1] *= 5/10 * ALPHA

def add_views():
    daniel[1] *= 10/10 * ALPHA
    grady[1] *= 4/10 * ALPHA
    francis[1] *= 5/10 * ALPHA
    kim_aziz[1] *= 10/10 * ALPHA
    maya_dan_seb[1] *= 10/10 * ALPHA
    kelly[1] *= 10/10 * ALPHA
    ari[1] *= 3/10 * ALPHA

def add_bonus():
    daniel[1] *= 10/10 * ALPHA
    grady[1] *= 6/10 * ALPHA
    francis[1] *= 2/10 * ALPHA
    kim_aziz[1] *= 0/10 * ALPHA
    maya_dan_seb[1] *= 0/10 * ALPHA
    kelly[1] *= 5/10 * ALPHA
    ari[1] *= 1/10 * ALPHA



if __name__ == "__main__":
    add_closet()
    add_natural_light()
    reduce_shared()
    # add_views()
    # add_bonus()
    get_prices()
