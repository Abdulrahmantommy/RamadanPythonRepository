
def roman_letter_value(letter):
    """
    Computes the decimal value of a roman number
    @param letter One character representing a roman number (M, D, C, L, X, V, I)
    @return The decimal numer  equivelant to the value of the character
    """
    return {
        "I" : 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
        }[letter]
  

def convert_roman_to_decimal(roman_number):
    """
    Computes the decimal value of a roman number
    @param rom_number The string of letters representing the roman number
    @return the decimal number equivelant to the roman number
    """
    decimal_value = 0
    repeat = len(roman_number)
    i = 0
    while(repeat>i):
        first_digit = roman_letter_value(roman_number[i])
        if repeat - i == 1:
            decimal_value = decimal_value + first_digit
            i+=1
        else:            
            second_digit = roman_letter_value(roman_number[i+1])
            if first_digit >= second_digit:
                decimal_value = decimal_value + first_digit
                i += 1
            else:
                decimal_value = decimal_value + (second_digit - first_digit)
                i += 2
    return decimal_value

print(convert_roman_to_decimal("MCMLXIX"))
            
