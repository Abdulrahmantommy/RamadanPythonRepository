#include<iostream>
#include<string>

std::string get_digit_char_code(int number); 
std::string get_number_code_string(int number); 
std::string get_number_barCode(int number); 

int main()
{
    int number = 0; 
    std::string barCode; 

    std::cout<<"Enter a 5-digit number to get its bar code or a non_number to quit:\n"; 
    while(std::cin>>number)
    {
        barCode = get_number_barCode(number); 
        std::cout<<"The bar code for "<<number<<": "<<barCode<<std::endl; 
        std::cout<<"Enter another number or a non-number to quit:\n"; 
        
    }
    return 0; 
}

/**
    Calculates a digit character numeric code as part of a larger program to get bar code
    @param number is the digit which is part of a large number
    @return numeric code for the digit as strings ex: 01001
*/
std::string get_digit_char_code(int number)
{
    std::string digitCode;
    std::string codeOne = "0", codeTwo="0", codeThree="0", codeFour="0", codeFive="0";
    int val = 0;
    int digit = 0;
    if(number == 0)
    {
        number = 11;
    }
    if (number >= 7)
    {
        digit = number / 7;
        codeOne = "1";
        val+=1;
        number = number % 7;
        digit = 0;
    }
    if (number >= 4)
    {
        digit = number / 4;
        codeTwo = "1";
        val+=1;
        number = number % 4;
        digit = 0;
    }
    if (number >= 2)
    {
        digit = number / 2;
        codeThree = "1";
        val+=1;
        number = number % 2;
        digit = 0;
    }
    if (number == 1)
    {
        codeFour = "1";
        val+=1;

    }
    if (val==1)
    {
        codeFive = "1";
    }

    digitCode = codeOne + codeTwo + codeThree + codeFour + codeFive;
    return digitCode;
}

/**
    Calculates a whole number string numeric code as part of a larger program to get bar code
    @param number is the number of 5 digits (ex: 19045) that will be changed
    @return numeric code for the number as as string ex: 010011100001001, should be thirty numerals
*/

std::string get_number_code_string(int number)
{
    std::string firstCode, secondCode, thirdCode, fourthCode, fifthCode, sixthCode;
    int firstVal=0, secondVal=0, thirdVal=0, fourthVal=0, fifthVal=0, sixthVal=0;
    int aggregateVal = 0;
    std::string numberCode;
    if (number <= 0)
    {
        return "";
    }
    else
    {
        firstVal = number / 10000;
        firstCode = get_digit_char_code(firstVal);
        aggregateVal+=firstVal;
        number = number % 10000;
        secondVal = number / 1000;
        secondCode = get_digit_char_code(secondVal);
        aggregateVal+=secondVal;
        number = number % 1000;
        thirdVal = number / 100;
        thirdCode = get_digit_char_code(thirdVal);
        aggregateVal+=thirdVal;
        number = number % 100;
        fourthVal = number / 10;
        fourthCode = get_digit_char_code(fourthVal);
        aggregateVal += fourthVal;
        number = number % 10;
        fifthVal = number;
        fifthCode = get_digit_char_code(fifthVal);
        aggregateVal += fifthVal;
        if (aggregateVal % 10)
        {
            int temp = aggregateVal % 10;
            sixthVal = 10 - temp;
            sixthCode = get_digit_char_code(sixthVal);
        }
        else
        {
            sixthVal = 0;
            sixthCode = get_digit_char_code(sixthVal);
        }
       numberCode = firstCode + secondCode + thirdCode + fourthCode + fifthCode + sixthCode;
    }
    return numberCode;

}
/**
    Generates a whole bar code with the help of other functions
    @param number is the number of 5 digits (ex: 19045) that will be changed
    @return bar code for the number as as string ex: |::|:||:::, should be thirty bars and colons
*/

std::string get_number_barCode(int number)
{
    std::string numberStringCode = get_number_code_string(number);
    std::string numberBarCode;
    for (int i = 0; i < numberStringCode.length(); i++)
    {
        if (numberStringCode[i]=='1')
        {
            numberBarCode += "|";
        }
        else
        {
            numberBarCode += ":";
        }
    }
    return numberBarCode;
}
