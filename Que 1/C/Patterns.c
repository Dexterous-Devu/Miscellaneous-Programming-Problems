#include<stdio.h>

void Right_angled_triangle(int);
void Isosceles_triangle(int);
void kite(int);
void half_kite(int);
void x(int);
void repeat(char, int);
void menu();


void repeat(char c, int num){
    printf(" ");
    for(int i=0; i<num; i++){
        printf("%c", c);
    }
}

void menu(){
    
    char b = '~';
    int a = 37, choice, size;

    repeat(b, a);
    printf("\n");

    printf(" *\t\tMENU\t\t     *\n");
    
    repeat(b, a);
    printf("\n");
    
    printf(" *  1. Right-angled Triangle\t     *\n *  2. Isosceles Triangle\t     *\n *  3. Kite\t\t\t     *\n *  4. Half Kite\t\t     *\n *  5. X\t\t\t     *\n");
    
    repeat(b, a);
    printf("\n");
    
    printf("\tEnter your Choice : ");
    scanf("%d", &choice);
    
    repeat(b, a);
    printf("\n");
    
    if ((choice == 1) || (choice == 2) || (choice == 3) || (choice == 4) || (choice == 5)){

        printf("\tEnter the Size : ");
        scanf("%d", &size);
        
        repeat(b, a);
        printf("\n");
        
        switch (choice){

            case 1:
                Right_angled_triangle(size);
                break;

            case 2:
                if(size % 2 == 0){
                    Isosceles_triangle(size);
                }else{
                    printf("     Size should be even number.");
                }
                break;
                
            case 3:
                if(size % 2 == 0){
                    kite(size);
                }else{
                    printf("     Size should be even number.");
                }
                break;
            
            case 4:
                half_kite(size);
                break;

            case 5:
                if(size % 2 == 0){
                    x(size);
                }else{
                    printf("     Size should be even number.");
                }
                break;
                
            default:
                printf("\t     Try Again!!!");
        }
    }else{
        printf("\t      Try Again!!!");
    }
    
    repeat(b, a);
    printf("\n");

}

void x(int n){
    char s = ' ';
    int count = n * 2;
        for(int i=1; i<=n; i++){
            repeat(s, i);
            for(int j=1; j<count; j++){
                printf("%d",j);
            }
            printf("\n");
            count -= 2;
        }

        count = 2;
        for(int i = n - 1; i>0; i--){
            repeat(s, i);
            count += 2;
            for(int j=1; j<count; j++){
                printf("%d",j);
            }
            printf("\n");
        }
    }


void half_kite(int n){
    int count = 1;
        for(int i=0; i<n; i++){
            for(int j=1; j<=count; j++){
                printf(" %d ",j);
            }
            count += 1;
            printf("\n");
        }
    count = n;
        for(int i=0; i<n-1; i++){
            for(int j=1; j<count; j++){
                printf(" %d ",j);
            }
            count -= 1;
            printf("\n");
        }
}

void kite(int n){
    Isosceles_triangle(n);
    char s = ' ';
    int count = n + 1;
        for(int i=2; i<=n; i++){
            repeat(s, i);
            for(int j=1; j<=count; j++){
                printf("%d",j);
            }
            count -= 2;
            printf("\n");
        }

}

void Isosceles_triangle(int n) {
    char s = ' ';
    int count = 1;
    for(int i=n; i>0; i--){
        repeat(s, i);
        for(int j=1; j<=count; j++){
            printf("%d",j);
        }
        count = count + 2;
        printf("\n");
    }

}

void Right_angled_triangle(int n){
    for(int i=1; i<=n; i++){
            printf("%s", "  ");
            for(int j=1; j<=i; j++){
                printf("%d ", j);
            }
            printf("\n");
        }
}

void main(){
    int n = 4, a = 1;
    char choice;

    while(a == 1){
        menu();
        printf("   Do you want to continue(Y/N) : ");
        scanf("%s", &choice);
        
        if (choice == 'y' || choice == 'Y'){
            a = 1;
        }else 
            a = 0;
        repeat('~', 37);
        printf("\n");
    }   

}