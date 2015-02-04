romanNumeralMap = 
              (('M',  1000),
               ('CM', 900),
               ('D',  500),
               ('CD', 400),
               ('C',  100),
               ('XC', 90),
               ('L',  50),
               ('XL', 40),
               ('X',  10),
               ('IX', 9),
               ('V',  5),
               ('IV', 4),
               ('I',  1))

def toRoman(n):
    if not (0 < n < 4000):
        raise OutOfRangeError("Tallet må være mellom 1-3999.")
    if int(n) != n:
            raise NotIntegerError("Ingen desimaler.")

    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result

    
    romanNumeralPattern = re.compile("""
    ^                   # beginning of string
    M{0,4}              # thousands - 0 to 4 M's
    (CM|CD|D?C{0,3})    # hundreds - 900 (CM), 400 (CD), 0-300 (0 to 3 C's),
                        #            or 500-800 (D, followed by 0 to 3 C's)
    (XC|XL|L?X{0,3})    # tens - 90 (XC), 40 (XL), 0-30 (0 to 3 X's),
                        #        or 50-80 (L, followed by 0 to 3 X's)
    (IX|IV|V?I{0,3})    # ones - 9 (IX), 4 (IV), 0-3 (0 to 3 I's),
                        #        or 5-8 (V, followed by 0 to 3 I's)
    $                   # end of string
    """ ,re.VERBOSE)

def toInt(s):
    """convert Roman numeral to integer"""
    if not s:
        raise InvalidRomanNumeralError('Fyll inn noe')
    if not romanNumeralPattern.search(s):
        raise InvalidRomanNumeralError('Ikke et romersk tall: %s' % s)

    result = 0
    index = 0
    for numeral, integer in romanNumeralMap:
        while s[index:index+len(numeral)] == numeral:
            result += integer
            index += len(numeral)
    return result