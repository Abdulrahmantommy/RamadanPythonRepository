#include<iostream>
#include<string>

int get_roman_number_val(std::string rnumber); 

int main()
{
	std::string roman_num; 
	std::cout<<"Enter a number in Roman format (ex: MDCVXI): \n"; 
	std::cin>>roman_num;
 	while(!std::cin.fail()){
		int decimal_value = get_roman_number_val(roman_num); 
		std::cout<<"The value of "<<roman_num<<" in decimal system = "<<decimal_value<<std::endl; 
		std::cout<<"Enter another Roman number or (0) to quit:"<<std::endl;
		std::cin>>roman_num; 
		 
	}
	 	

	return 0; 
}

/**
    Computes the decimal value of a Roman character digit
    @param rnum The Roman character digit 
    @return the decimal numeric value of the Roman digit
*/
int convert_roman_numbers(char rnum)
{
    int val = 0;
    if(rnum == 'I')
    {
        val = 1;
    }
    else if(rnum == 'V')
    {
        val = 5;
    }
     else if(rnum == 'X')
    {
        val = 10;
    }
     else if(rnum == 'L')
    {
        val = 50;
    }
     else if(rnum == 'C')
    {
        val = 100;
    }
     else if(rnum == 'D')
    {
        val = 500;
    }
     else if(rnum == 'M')
    {
        val = 1000;
    }
    return val;
}

/**
    Computes the decimal value of a Roman number
    @param rnumber The Roman character number 
    @return the decimal numeric value of the Roman number
*/
int get_roman_number_val(std::string rnumber)
{
    int integer_value = 0;
    int repeat = rnumber.length();
    int i = 0;
    while(repeat > i)
    {
        char sfirst = rnumber.at(i);
        int first = convert_roman_numbers(sfirst);
        if(repeat - i == 1)
        {
            integer_value += first;
            i++;
        }
        else
        {
            char sSecond = rnumber.at(i+1);
            int second = convert_roman_numbers(sSecond);
            if(first >= second)
            {
                integer_value += first;
                i++;
            }
            else
            {
                integer_value += (second - first);
                i = i + 2;
            }
        }
    }

    return integer_value;
}
