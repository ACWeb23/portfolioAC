package mar21;

import java.util.Scanner;

public class twenty 
{
	static int buyItem(int money, int price, String itemName) 
	{
		System.out.println("George");
		if (price <= money)
		{
			money -= price;
			System.out.println(itemName + ": Purchaced");
		}
		else
		{
			System.out.println("Not Enouch Money");
		}
		return money;
	}
	static int looseLive(int numLives)
	{
		if(numLives > 0)
		{
			-- numLives;
		}
		return numLives;
	}
	static boolean digitCheck(int num)
	{
		int x = num;
		if (x >= 0 || x <10)
		{
			System.out.println("Digit");
			return true;
		}
		else 
		{
			return false;
		}
	}
	static int sum(int[] nums)
    {
        int numbers[] = nums;
		int sum = 0; // initialize sum
        int i;
 
        // Iterate through all elements and add them to sum
        for (i = 0; i < numbers.length; i++)
        {
            sum += numbers[i];
        }
        System.out.println("Sum = " + sum);
        return sum;
    }
	static int product(int[] nums)
    {
        int numbers[] = nums;
		int product = 1; // initialize sum
        int i;
 
        // Iterate through all elements and add them to sum
        for (i = 0; i < numbers.length; i++)
        {
            product = product * numbers[i];
        }
        System.out.println("Product = " + product);
        return product;
    }
	
	static boolean guessCode(int add, int multiply)
	{
		int sum = add;
		int product = multiply;
		boolean goodGuess = false;
		if(sum == 13)
			if(product == 48)
			{
				 goodGuess = true;
				 System.out.println("Good Guess");
			}
			else
			{
				goodGuess = false;
				System.out.println("Bad Guess");
			}
		else 
		{
			goodGuess = false;
			System.out.println("Bad Guess");
		}
		return goodGuess;
	}
	static boolean mosquitoBomb(boolean saved)
	{
		boolean goodGuess = saved;
		if(goodGuess == false) 
		{
			System.out.println("Failure the world is cured of mosquitos");
			return false;
		}
		return goodGuess;
	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int m = 1000;
		int p = 250;
		String Item = "MP Potion";
		
		m = buyItem(m,p,Item);
		System.out.println("money = $" + m);
	
		int numbers[]= {0,0,0,0};
		Scanner myObj = new Scanner(System.in); // Create a Scanner object
		for(int i = 0; i < numbers.length; i++)
		{
			boolean goodDigit = false;
			while(goodDigit == false) 
			{
				System.out.println("Enter digit number " + (numbers.length -  (numbers.length - 1)+ i) + ": ");
			    String number1 = myObj.nextLine();
			    numbers[i] = Integer.parseInt(number1);
			    goodDigit = (digitCheck(numbers[i]));
			}
			
		}
		
		myObj.close();
		mosquitoBomb(guessCode(product(numbers), sum(numbers)));

		
	    	
	

	}


}
