import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.ImageIcon;

/*
 * We need to declare the Kart class here:
 * The Kart class should inherit from the Actor class.
 */
class Kart extends Actor {
	String name;
	int lives;
	int coins; 
	int raceRank;
	int speed;
	int maxSpeed;
	int acceleration;
	int lapNumber;
	int maxLaps;
	private int currentTime;
	private int[] lapTimes;
	double theta;
	int totalTime;

	public Kart(String img, double x, double y, String n, int acc, int maxS, int rR) 
	{
		super(img, x, y);
		lives = 3;
		coins = 0;
		raceRank = rR;
		speed = 0;
		maxSpeed = maxS;
		name = n;
		acceleration = acc;
		lapNumber = 1;
		maxLaps = 5;
		currentTime = 0;
		lapTimes = new int[maxLaps];
		totalTime = 0;
		
	}
	// Increasing Speed
	public void increaeSpeed()
	{
		speed += acceleration;
		if (speed > maxSpeed)
		{
			speed = maxSpeed;
		}
	}	
	// Decrease Speed
	void decreaseSpeed()
	{
		speed -= acceleration;
		if (speed < 0)
		{
			speed = 0;
		}	
	}
	// Increase Laps
	void increaseLap()
	{

		if(lapNumber > maxLaps)
		{
			System.out.println("Cannot increase lap - already at max number of laps!");
		}
		else
		{
			lapTimes[(lapNumber - 1)] = currentTime;
			currentTime = 0;
			lapNumber += 1;
		}
	}
	// Time
	void incTime()
	{
		currentTime +=1;
		totalTime += 1;
	}
	// Getting current time
	int getCurrentTime()
	{
		return currentTime;
	}
	// getting time for a Lap
	int getLapTime(int lIndex)
	{
		int lapIndex = 0;
		if (lIndex > (maxLaps + 1))
		{
			lIndex -=1;
			if (lIndex <= lapTimes.length && lIndex <= 0)
			lapIndex = lapTimes[lIndex];
		}
		return lapIndex;
	}
	
	int getBestTime()
	{
		int best = 0;
		for(int i = 0; i < lapTimes.length; i++)
		{
			if(lapTimes[i]> best)
			{
				best = lapTimes[i];
			}
		}
		System.out.println("best Lap Time Is " + best);
		return best;
	}
	int getWorstTime() 
	{
		int worst = 2147483647;
		for (int i = 0; i < lapTimes.length; i++)
		{
			if(lapTimes[i] < worst)
			{
				worst = lapTimes[i];
			}
		}
		System.out.println("Worst Time Is " + worst);
		return worst;
	}
	
}

/*****************************************************************************
    // This part should not be modified
    * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
public class Actor {
	public double x;
	public double y;
        public int width;
	public int height;
        public int angle;
        private String image;
        private Image i;


	public Actor(String img) {
            changeImage(img); 
            angle = 0;
	}
        
        public Actor(String img, double a, double b) {
            x = a;
            y = b;
            angle = 0;
            changeImage(img); 
	}
        
        public String getImage(){
            return image;
        }
                
        public void changeImage(String img) {
            image = img;
            String separator = System.getProperty("file.separator");
            i = new ImageIcon("images" + separator + image + ".png").getImage();
            width = i.getWidth(null);
            height = i.getHeight(null);
	}

	public void draw(Graphics2D g) {
            if (angle!=0)
                g.rotate(Math.toRadians(-angle),x - i.getWidth(null)/2, y - i.getHeight(null)/2);
                
            g.drawImage(i, (int)x, (int) y, null);
	}
}