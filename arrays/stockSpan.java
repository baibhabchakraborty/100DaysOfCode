import java.util.Scanner;
import java.util.Stack;

public class stockSpan
{   

    public static int[] calculateSpan(int price[], int n)
    {
        int span[]  = new int[n];
        span[0] = 1;
        
        for(int i=1;i<n;i++)
        {
            span[i] = 1;
            for(int j=i;(j>=0)&&(price[i]>=price[j]);j--)
                span[i]++;
        }
        return span;
    }


    public static void main(String[] args)
    {
        Scanner S = new Scanner(System.in);
        int t = S.nextInt();

        while(t-- > 0)
        {   
            int n = S.nextInt();
            int a[] = new int[n];

            int i = 0;
            for(i=0;i<n;i++)
            {
                a[i] = S.nextInt();
            }
            int s[] = new int[100];

            s = calculateSpan(a,n);

            for(i=0;i<n;i++)
            {
                System.out.println(s[i] + " ");
            }
            S.close();
        }
    }
}