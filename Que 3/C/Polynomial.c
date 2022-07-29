#include<stdio.h>
#include<stdlib.h>
#include<math.h>

#define MAX 3

void polynomial_func(int, int [], int, int , int);
void _print_(char, int);

// This Function prints the characters in the row continously according to the given number.
void _print_(char a, int calc){
    for(int k=0; k<calc; k++){
        printf("%c", a);
    }
    printf("\n");
}

// This Function provide a value from( lower bound to upper bound ) to the polynomial expression that generates a value. 
// that value is passsed to the _print_() function to print the '*' Pattern.
void polynomial_func(int n, int arr[], int lower_bound, int upper_bound, int incr){
    
    int calc;

    for(int i=lower_bound; i<=upper_bound; i = i + incr){

        calc = 0;
        printf("| ");

        for(int j=n; j>=0; j--){
            calc += pow(i, j) * arr[n - j];                 // Calculating the value of the polynomial function acc. to the Inputs given by the user.
        }
        _print_('*', calc);
    }
}


int main(){

    int n, arr[MAX], lower_bound, upper_bound, incr;
    int m = 57;
    
    printf("\n");

    _print_('-', m);
    printf("|\t\tPOLYNOMIAL FUNCTION PROBLEM\t\t|\n");
    _print_('-', m);
    
    printf("|\t    Provide Polynomial Function Details:\t|\n");
    _print_('-', m);

    printf("  Enter degree of Polynomial (MAX=3): ");               // Taking the degree of the polynomial function as input from the user.
    scanf("%d", &n);
    _print_('-', m);

    for(int i=0; i<=n ; i++){
        printf("  ->  coeff %d: ", i + 1);
        scanf("%d", &arr[i]);
    }

    _print_('-', m);
    printf("  Provide lower bound for x: ");
    scanf("%d", &lower_bound);
    
    printf("  Provide upper bound for x: ");
    scanf("%d", &upper_bound);

    printf("  Provide number of steps, you wish to increment x: ");
    scanf("%d", &incr);

    _print_('-', m);
    printf("\n");

    // Calling print_pattern function.
    polynomial_func(n, arr, lower_bound, upper_bound, incr);              
    
    printf("\n");
    _print_('-', m);
    printf("\n");
}