package review;

public class inventoy{
	String weapInventory[][]= {{"empty","empty","empty","empty","empty","empty","empty","empty","empty","empty"},{"empty","empty","empty","empty","empty","empty",},{"empty","empty",}};
	String weapTypes[] = {"Blade","Grenade", "Rock"};
	int type;
	int number;
	
	static void addItem(int type, int number)
	{
		int wepType = type;
		int subBag = wepType - 1;
		int num = number;
		int originalNum = number;
		int storedK = 0;
		int storedKPost = 0;
		int numberCount = 0;
		while (num >0)
		{
			if(weapInventory[subBag][numberCount]!= "empty")
			{
				weapInventory[subBag][numberCount] = weapTypes[subBag];
				storedKPost += 1;
			}
			numberCount +=1;
			num -= 1;
			if (num == 0)
			{
				System.out.println(originalNum +" "+ weapTypes[subBag] + "Stored");
			}
		}
		// Grenades
		if(type == 2)
		{
			for(int i = 0; i <= weapInventory[1].length; i++)
			{
				if(weapInventory[1][i]!= "empty")
				{
					weapInventory[1][i] = "blade";
					storedKPost += 1;
				}
			}
			if (storedKPost > storedK)
			{
				System.out.println(storedKPost + "Grenades Stored");
			}
			else
			{
				System.out.println("Grenade Inventory Full");
			}
		}
		if(type == 3)
		{
			for(int i = 0; i <= weapInventory[2].length; i++)
			{
				if(weapInventory[2][i]!= "empty")
				{
					weapInventory[2][i] = "blade";
					storedKPost += 1;
				}
			}
			if (storedKPost > storedK)
			{
				System.out.println(storedKPost + "Rocks Stored");
			}
			else
			{
				System.out.println("Rocks Inventory Full");
			}
		}
		
			
	}
	void emptyBag()
	{
		System.out.println("Inventory Empty"); 
		String weapInventory[][] = {{"empty","empty","empty","empty","empty","empty","empty","empty","empty","empty"},{"empty","empty","empty","empty","empty","empty",},{"empty","empty",}};
	}
	void dropItem(int type)
	{
		int counter = 1;
		int typeSelect = type-1;
		for(int i = 0; i <= weapInventory[typeSelect].length; i++ )
		{
			if(weapInventory[typeSelect][i] != "empty")
			{
				if(counter == 1)
				{
					weapInventory[typeSelect][i] = "empty";
					counter = 0;
				}
			}
			
		}
		if (counter == 1) 
		{
			System.out.println("inventory Full");
		}
		else if (counter == 0)
		{
			System.out.println("Item Stored");
		}
		else if (counter != 0 && counter != 1)
		{
			System.out.println("Error: Counter out of range");
		}
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for (int i= 0; i <= inventoy[][].length; i++)
		{
			System.out.println(inventoy.weapInventory);
		}
		System.out.println(inventoy.weapInventory);
		int x = 2;
		int y = 6;
		int z = 2;
		inventoy.addItem(x,z);
		System.out.println(inventoy.weapInventory);
		

	}

}
