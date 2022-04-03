import java.util.Scanner;
import java.util.Arrays;

public class find3Nos {
    
    public static int find3Numbers(int A[], int n, int X)
    {
        Arrays.sort(A);
        for(int i=0;i<n;i++)
        {
            int y=X-A[i];
            int low = i+1;
            int high = n-1;
            while(low<high)
            {
                if(A[low]+A[high]==y)
                {
                    return 1;
                }
                else if(A[low]+A[high]>y)
                {
                    high--;
                }
                else if(A[low]+A[high]<y)
                {
                    low++;
                }
            }
        }
        return 0;
    }
    
    
    public static void main(String[] args) 
    {
        Scanner S = new Scanner(System.in);
        System.out.println("Enter the length of array:");
        int n = S.nextInt();
        int A[] = new int[n];
        System.out.println("Enter the array");
        for(int i=0;i<n;i++)
        {
            System.out.println("Enter array element:");
            A[i] = S.nextInt();
        }

        System.out.println("Enter key element:");
        int X = S.nextInt();
        int f = find3Numbers(A,n,X);
        if(f==1)
        {
            System.out.println("Found!");
        }
        else
        {
            System.out.println("Not found");
        }
        S.close();
    }
}
