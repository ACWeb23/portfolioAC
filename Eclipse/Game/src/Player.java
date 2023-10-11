import java.io.File;
import java.util.Scanner;

class Mage 
{
	int speed;
	String name;
	int hp;
	int hunger;
	int thirsty;
	int stamina;
	int mana;
	int range;
	float xPos;
	float yPos;
	Boolean sprint;
	Boolean isHit;
	Boolean walking;
	Boolean standing;
	Boolean sleeping;
	Boolean sitting;
	Boolean alive;
	
	
	
	Mage(String name)
	{
		speed = 10;
		name = "";
		hp = 100;
		hunger = 100;
		thirsty = 100;
		stamina = 100;
		mana = 250;
		range = 100;
		xPos = 0.0f;
		yPos = 0.0f;
		sprint = false;
		isHit = false;
		walking = false;
		standing = true;
		sleeping = false;
		sitting = false;
		alive = true;
		
		
		
	}
	boolean isHungry()
	{
		if (hunger >= 20)
				return false;
		else
			return true;
	}
	
	boolean isTired()
	{
		if (stamina <= 10)
			return true;
		else
			return false;
	}
	
}
public class Player {

	public static void main(String[] args) {
		Scanner myObj = new Scanner(System.in);
		System.out.println("Enter username");
		String namePlayer = myObj.nextLine();
		Mage Player = new Mage(namePlayer);
		
		

	}

}
