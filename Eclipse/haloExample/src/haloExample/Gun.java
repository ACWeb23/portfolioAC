package haloExample;
public class Gun
{
	public String name;
	public int magnification;
	public String attackSpeed;
	public boolean type;
	public int bulletPunch;
	public int ammunition; 
	public String image;
	public float overHeat;
	public double xPos;
	public double yPos;
	public double zPos;
	
	public Gun(int mag, String atkSpeed,  boolean weapType, int punch, int ammo, String img, float heat)
	{
		magnification = mag;
		attackSpeed = atkSpeed;
		type = weapType;
		ammunition = ammo;
		image = img;
		overHeat = heat;
	}
	public void typeSel(boolean weapType)
	{
		type = weapType;
		if(type)
		{
			System.out.println("Plasma");
			ammunition = 1000;
			overHeat = (float)ammunition;
			System.out.println("Overheat");
			bulletPunch = 0;
			attackSpeed = "";
			
		}
	}
}

class Pistol 
{
	String name = "Pistol";
	int magnification = 2;
	String attackSpeed = 'Medium';
	boolean type = false;
	int bulletPunch = 5;
	int ammunition = 12; 
	String image = "pistol";
	float overHeat = 0.0f;
	float angle = 0.0f; // use player postion 
}
class kineticRifle
{
	
}
class sniperRifle
{
	
}
class rocketLauncher
{
	
}
class plasmaRifle
{
	
}
class plasmaPistol
{
	
}
class zoom
{
	
}