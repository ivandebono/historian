"""
Ivan Debono
October 2017

A collection of useful codes for historians
"""

def indiction(year,calendar='AD'):

    """Calculate the indiction, given the year
    """

    if calendar == 'AD':    # Julian Anno Domini
        indiction=((year + 2) % 15) + 1
        print('Anno Domini',year,'Indictionis',arabic2roman(indiction))

    elif calendar == 'AM':  # Byzantine Anno Mundi
        am=year+5508
        indiction = am % 15
        if indiction == 0 : indiction = 15
        print('Anno Mundi',am,'Indictionis',arabic2roman(indiction))


    return indiction



def arabic2roman(num):

    """Convert Arabic numerals to Roman
    """

    from collections import OrderedDict

    rmn = [  (1000, "M"),
             (900 , "CM"),
             (500 , "D"),
             (400 , "CD"),
             (100 , "C"),
             (90  , "XC"),
             (50  , "L"),
             (40  , "XL"),
             (10  , "X"),
             (9   , "IX"),
             (5   , "V"),
             (4   , "IV"),
             (1   , "I")
             ]
    roman = OrderedDict(rmn)   

    def roman_num(num):
        for r in roman.keys():
            x, y = divmod(num, r)
            yield roman[r] * x
            num -= (r * x)
            if num > 0:
                roman_num(num)
            else:
                break

    return "".join([a for a in roman_num(num)])
