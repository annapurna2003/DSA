import java.util.*;
class linear_search
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        System.out.println("ennter numberof elements");
        int n,c,f,flag;
        n=sc.nextInt();
        int[] array=new int[n];
        System.out.println("Enter the elements of the array");
        for(c=0;c<n;c++)
        {
            array[c]=sc.nextInt();
        }
        System.out.println("Enter the value to be searched in the array");
        f=sc.nextInt();
        flag=0;
        for(c=0;c<n;c++)
        {
            if(array[c]==f)
            {
                System.out.println("The element is found in the location "+(c+1));
                flag=1;
                break;
            }
        }
        if(flag==0)
        {
            System.out.println("The element to be searched is not found in the given array");
        }
    }
}
