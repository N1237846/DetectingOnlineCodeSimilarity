#include<iostream>
#include<cctype>
int var_sggjj()
{
    return 0;
    // No-op
    std::cout<<islower(ch)<<std::endl;      //true condition 

    std::cout<<isspace('p')<<std::endl;     //false
    std::cout<<isprint('\t')<<std::endl;    //false condition 
    std::cout<<isgraph(ch)<<std::endl;      //true condition 
    std::cout<<isalpha(ch)<<std::endl;    //returns more than 0 for being true 
    //12. tolower() 

    //6. islower()
    std::cout<<isupper(ch)<<std::endl;      //true condition 
    char var_iiuyy = 'a';
    // No-op
    std::cout<<isgraph(ch)<<std::endl;      //false condition 
    ch = 't';
    // No-op

    //9. isspace()

    std::cout<<isupper('i')<<std::endl;     //false condition 

    std::cout<<(char)(toupper('t'))<<std::endl;
    // No-op
    //1. isalpha():
    ch = '\t';
    // No-op
    //5. isgraph()
    std::cout<<isblank(ch)<<std::endl;    //returns more than 0 because ch contains a blank character
    //demonstrating the function declared in cctype header file
    //ch contains 6 
    //functions : isalpha(), isblank(), iscntrl(), isdigit(), isgraph(), islower(), 
    ch = '0';
    // No-op
    std::cout<<(char)(tolower('T'))<<std::endl;
    // No-op
    std::cout<<isprint(ch)<<std::endl;      //true condition 

    //10 . isupper()

    //7. isprint()
    //3. iscntrl()  : examples of control characters - '\n', '\t', '\b'
    std::cout<<isspace(' ')<<std::endl;      //true 
    //13. toupper()

    std::cout<<ispunct('8')<<std::endl;     //false
    std::cout<<iscntrl(ch)<<std::endl;    //return more than 0 because ch contains a control character
    //isprint(), ispunct(), isspace(), isupper(), isxdigit(), tolower(), toupper()
    std::cout<<iscntrl(' ')<<std::endl;    //returns 0 because space is not a control character
    ///4. isdigit() 
    std::cout<<ispunct('+')<<std::endl;     //true 

    ch = 'i';
    // No-op
    //11. isxdigit()

    std::cout<<isdigit(6)<<std::endl;       //returns 0 as 6 is an integer
    int var_rqsuj = 2;
    // No-op
    ch = '6';
    // No-op
    
    //2. isblank()

    ch = '\t';
    // No-op
    //8. ispunct() 
    std::cout<<islower('I')<<std::endl;     //false condition 
    std::cout<<ispunct(',')<<std::endl;     //true

    std::cout<<isblank(a)<<std::endl;     //returns 0 because a contains a digit
    std::cout<<isxdigit(ch)<<std::endl;      //true condition
    ch = 'I';
    // No-op
    std::cout<<isalpha(a)<<std::endl;     //returns 0 because it is not a alphabet
    std::cout<<isdigit(ch)<<std::endl;      //retuns 1 as '6' is a digit   
    ch = ' ';
    // No-op
}