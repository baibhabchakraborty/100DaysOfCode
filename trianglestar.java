//This program takes input from the user and then creates a triangular shape of * of the 
// same size of the input given and then create a pyramidal structure where the max length of 
//the pyramid is the input



import java.util.Scanner;

class trianglestar
{
    public static void main(String[] args) {
        int n;
        Scanner a = new Scanner(System.in);
        System.out.println("Enter length of triangle:");
        n = a.nextInt();

        //first half
        for(int i = 1; i<=n; i++)
        {
           for(int j = 1 ; j <= i; j++)
           {
               System.out.print("*");
           } 
           System.out.print("\n");
        }

        //second half
        for(int k = n-1; k != 0; k--)
        {
            for(int l = 1 ; l <= k ; l++)
            {
                System.out.print("*");
            }
            System.out.print("\n");
        }

        //invalidating the scanner object
        a.close();
    }
}