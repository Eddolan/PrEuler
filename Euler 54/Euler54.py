__author__ = 'Eddie'


def get_hands( filename ):
    return [ [hands.split()[0:5] , hands.split()[5:10]] for hands in open( filename , 'r' ).read().split('\n') ]

def iterator( hands_list ):
    count = 0
    for hand in hands_list:
        x =  get_points( hand[0] )
        y =  get_points( hand[1] )
        if x - y > 0:
            print hand
            count = count +  1
        if x - y == 0:
            tie_break = tie(hand[0]) - tie(hand[1])
            if tie_break > 0:
                count = count + 1
    print count

def tie(hand):
    maybel = [ int( get_value( card )  ) for card in hand ]
    maybel.sort()
    maybel.reverse()
    maybel1  = [int(maybel.count(x)) for x in maybel]
    if 2 in maybel1:
        return maybel[maybel1.index(2)]
    max_val = max(maybel1)
    return maybel[maybel1.index(max_val)]
def get_points( hand ):
    scoring =  [  "Maybel" , pair(hand) , t_pair(hand) , three(hand) , straight(hand) ,\
                  flush(hand) , full(hand) , FOAK(hand) , straight_flush(hand)]
    scoring[0] = scoring.count( True ) == 0
    return  (8 - scoring[::-1].index(True)) * 52
def high_card( hand ):
    return max( [ int( get_deck_points( card )  ) for card in hand ])
def pair( hand):
    vals = [ int( get_value( card[0] )  ) for card in hand ]
    maybel = [ vals.count( value ) for value in  vals ]
    return maybel.count(2) == 2
def t_pair( hand):
    suits = [ int( get_value( card[0] )  ) for card in hand ]
    maybel = [ suits.count( value ) for value in  suits ]
    return maybel.count(2) == 4 and maybel.count(1) == 1
def three( hand):
    suits = [ int( get_value( card[0] )  ) for card in hand ]
    maybel = [ suits.count( value ) for value in  suits ]
    return  maybel.count( 3 ) == 3
def straight( hand ):
    suits = [ int( get_value( card[0] )  ) for card in hand ]
    suits.sort()
    if suits[4] - suits[0] == 4 and  not pair(hand) and not three(hand) and not t_pair(hand ):
        return True
    return False
def flush( hand ):
    suits = [ int( get_suit( card )  ) for card in hand ]
    suits.sort()
    if suits[4] - suits[0] == 0:
        return True
    return False
def full( hand ):
    x =  three( hand ) and pair( hand )
    return x
def FOAK( hand ):
    suits = [ card[0] for card in hand ]
    if suits.count( suits[0] ) == 4 or suits.count( suits[1] ) ==4:
        return True
    return False
def straight_flush( hand ):
    if flush( hand ) & straight( hand ):
        return True
    return False

def get_deck_points ( card ):
    return get_suit( card ) * 13 + get_value( card )
def get_suit( card ):
    return "CDHS".index( card[1] )
def get_value( card ):
    return "23456789TJQKA".index( card[0] )

def main():
    hands = get_hands( 'poker.txt' )
    iterator( hands )

main()