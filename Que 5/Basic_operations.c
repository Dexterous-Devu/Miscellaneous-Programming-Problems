#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>             // importing stdbool.h header file which allows us to use Boolean Data Type.
#include<math.h>                // importing Math Library for performing mathematical operations.


int reverseNumber(int);
bool checkPalindrome(int);
bool checkNarcissistic(int, int);
int _count_(int);
int findDigitSum(int);
int findSquareDigitSum(int);
bool menu(int, int, int, char);
void repeat(char, int);


/*
    This Function returns the Sum of Square of Digits of a Number e.g. 12 => (1^2)+(2^2) = 5.
    If the Sum of Square of the Digits of the Number is of Single digit then it will return the Sum,
    otherwise, 
    The function will call itself until the Sum is of single digit and keep on adding all the sums.
*/
int findSquareDigitSum(int n){

    int sum = 0, sum_count;
    int count = _count_(n);

    while(n != 0){
        sum += pow((n%10), 2);
        n /= 10;
    }

    sum_count = _count_(sum);

    if (sum_count == 1)
        return sum;

    else{
        return (sum + findSquareDigitSum(sum));
    }
}


/*
  This Function returns the Sum of Digits of a Number e.g. 1071 => 1+0+7+1 = 9.
  If the Sum is of the Number is of single digit then it will return the Sum otherwise 
  the function will call itself until the Sum is of single digit and keep on adding all the sums.
  e.g. (89) = 8+9 = 17, sum = 17
       (17) = 1+7 = 8, sum = 17 + 8 => sum = 25.
*/
int findDigitSum(int n){

    int sum = 0, sum_count;
    int count = _count_(n);

    while(n != 0){
        sum += (n%10);
        n /= 10;
    }

    sum_count = _count_(sum);

    if (sum_count == 1)
        return sum;
    
    else{
        return (sum + findDigitSum(sum));
    }
}


//  This Function returns the no. of digits of the given number e.g. 1071 => no. of digits = 4.
int _count_(int n){
    
    int count = 0;

    do{
        n /= 10;
        ++count;
    }while (n!=0);

    return count;
}


/*
  This Function returns the Boolean value that the number is Narcissistic or not.
  e.g. 153 = 1^3 + 5^3 + 3^3 => 153. (no. of digits = 3)
  The Number is processed through some mathematical operation i.e. 
  The Sum of the nth power of the Digits, where n: Number of Digits.
*/
bool checkNarcissistic(int n, int count){
    
    int sum = 0, rem, original = n;

    while(n != 0){
        
        rem = n % 10;
        sum += pow(rem, count);
        n /= 10;
    }

    if (original == sum) return true;
    else return false;
}


/*
 This Function return the Boolean value that the number is Palindrome or not.
 e.g. 12321 is Palindrome because the reverse of the number is equal to the original number.
 original_Number = reverse_Number = 12321
*/
bool checkPalindrome(int n){

    int reverse;
    
    reverse = reverseNumber(n);
    
    if (n == reverse) 
        return true;
    else 
        return false;
}


//  This Function return the reverse number of the original number e.g. 12345, reverse_Number = 54321.
int reverseNumber(int n){

    int rem, reverse = 0;
    
    while (n != 0){
    
        rem = n % 10;
        n /= 10;
        reverse = reverse * 10 + rem;
    
    }
    return reverse;
}   


// This function prints the character repeatedly according to the given values.
void repeat(char c, int num){
    printf(" ");
    for(int i=0; i<num; i++){
        printf("%c", c);
    }
    printf("\n");
}


// This is the Menu function of the Application.
bool menu(int n, int count, int m, char c){
    int choice, result;
    
    repeat(c, m);
    printf("|\t\t    Welcome to the Application.\t\t\t  |\n");
    repeat(c, m);
    printf("|\t   Please select one of the following operation.\t  |\n");
    repeat(c, m);

    printf("| 1. Find Reverse of a number.\t\t\t\t\t  |\n");
    printf("| 2. Check whether a number is a Palindrome or not.\t\t  |\n");
    printf("| 3. Check whether a number is a Narcissistic number or not.      |\n");
    printf("| 4. Find the Sum of digits of a Number.\t\t\t  |\n");
    printf("| 5. Find the Sum of Squares of digits of a number.\t\t  |\n");
    printf("| 6. Exit\t\t\t\t\t\t\t  |\n");

    repeat(c, m);

    printf("  -> Select an operation : ");
    scanf("%d", &choice);

    if (choice == 6) return false;

    repeat(c, m);

    printf("  -> Enter the number    : ");
    scanf("%d", &n);
    repeat(c, m);

    count = _count_(n);

    switch (choice){

        case 1:
            printf("|\t      You've Selcted Reverse Number Operation.  \t  |\n");
            repeat(c, m);
            printf("\n");
            printf("  * Number          : %d\n", n);
            printf("  * Reverse Number  : %d\n", reverseNumber(n));
            break;

        case 2:
            printf("|\t      You've Selcted Palindrome Number Checker.  \t  |\n");
            repeat(c, m);
            printf("\n");
            printf("  * Number      : %d\n", n);
            result = checkPalindrome(n);
            printf("  * Result      : ");
            if (result == 1){ 
                printf("True\n\n");
                printf("\t\t  *** THE NUMBER IS PALINDROME. ***\n");
            }
            else{ 
                printf("False\n\n");
                printf("\t\t  *** THE NUMBER IS NOT PALINDROME. ***\n");
            }
            break;

        case 3:
            printf("|\t      You've Selcted Narcissictic Number Checker.  \t  |\n");
            repeat(c, m);
            printf("\n");
            printf("  * Number      : %d\n", n);
            result = checkNarcissistic(n, count);
            printf("  * Result      : ");
            if (result == 1){ 
                printf("True\n\n");
                printf("\t\t  *** THE NUMBER IS NARCISSICTIC NUMBER. ***\n");
            }
            else{ 
                printf("False\n\n");
                printf("\t\t  *** THE NUMBER IS NOT NARCISSICTIC NUMBER. ***\n");
            }
            break;

        case 4:
            printf("|      You've Selcted Sum of Digits of Number operation.  \t  |\n");
            repeat(c, m);
            printf("\n");
            printf("  * Number                   : %d\n", n);
            result = findDigitSum(n);
            printf("  * Sum of digits of Number  : %d\n", result);            
            break;

        case 5:
            printf("|   You've Selcted Sum of Square of Digits of Number operation.  |\n");
            repeat(c, m);
            printf("\n");
            printf("  * Number                             : %d\n", n);
            result = findSquareDigitSum(n);
            printf("  * Sum of Sqaure of digits of Number  : %d\n", result);
            break;

        case 6:
            return false;

        default:
            printf("Try Again.");
    }

    printf("\n");
    repeat(c, m);
    printf("\n");
    menu(n, count, m, c);
}


int main(){

    int n, count, m=65, choice;
    char c = '-'; 

    printf("\n");
    menu(n, count, m, c);
    repeat(c, m);
    printf("\n");

    return 0;
}