import java.awt.Color;
import java.awt.Font;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.RenderingHints;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import javax.swing.ImageIcon;
import javax.swing.JPanel;

/*
 * Please enter your information.
 * Name: Andrew Coleman
 * CWID#: 50298859
 */
public class Game extends JPanel implements KeyListener{
    public int WIDTH;
    public int HEIGHT;
    // Declare the 2 arrays here
    String trackNames[] = {"MARIO CIRCIT", "CHOCO ISLAND", "DONUT PLAINS", "BOWSER CASTLE", "GHOST VALLEY", "VANILLA LAKE"};
    String trackImages[] = {"t0","t1","t2","t3","t4","t5"};
    Actor mario;
    
    Boolean gameRun = true;
    int selectY = 80;
    
    public void init() {
        // Initialiaze the variables here
    	WIDTH = 1000;
        HEIGHT = 800;
        mario = new Actor("Mario", 484.0, 80.0);
        mario.selection = 0;
        
    }
  
    public void draw(Graphics2D screen) 
    {
    	selectY = 108;
        screen.setColor(Color.WHITE);
        screen.setFont(new Font("Verdana", Font.BOLD, 30));
        // Draw Background:
        blit(screen, "bground",1.0,1.0);
        
        // Draw Track:
        blit(screen,trackImages[mario.selection],1.0,399.0);
        screen.drawString("COURSE SELECT.", WIDTH/8, HEIGHT/8);
        // Draw Mario:
        blit(screen,mario.getImage(),mario.x,mario.y);
        // Let us use a loop to write the names of the tracks on the screen:
        for (int i = 0; i < 6; i++)
        {
        	screen.drawString(trackNames[i],532,selectY);
        	selectY += 48.0;
        }
        /*while(gameRun == true)
        {
        	System.out.println("Run");
        }
        */
    }
    
    @Override
    public void keyReleased(KeyEvent e) 
    {
        // to be completed in Section 3
    	if (e.getKeyCode() == KeyEvent.VK_UP)
    	{
    		mario.selection += 1;
    		if(mario.selection > 5)
    		{
    			mario.selection = 0;
    		}
    		mario.y -= 48;
    		if (mario.y < 80.0)
    		{
    			mario.y = 320.0;
    		}
    	}
    	else if (e.getKeyCode() == KeyEvent.VK_DOWN)
    	{
    		mario.selection -= 1;
    		if(mario.selection < 0)
    		{
    			mario.selection = 5;
    		}
    		mario.y += 48;
    		if (mario.y > 320.0)
    		{
    			mario.y = 80.0;
    		}
    	}
    }
        
 /*****************************************************************************
    // This part should not be modified
    * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
    
    public Game() 
    {
        setBackground(Color.black);
        setSize(WIDTH, HEIGHT);
        addKeyListener(this);
        setFocusable(true);
        init();
    }
    
        public void blit(Graphics g, String img, double x, double y) {
            String separator = System.getProperty("file.separator");
            Image i = new ImageIcon("images" + separator + img + ".png").getImage();
            g.drawImage(i, (int)x, (int)y, null);
    }

    @Override   
    public void paint(Graphics g) {
        super.paint(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);
        draw(g2d);
    }

    @Override
    public void keyPressed(KeyEvent e) 
    {
    	
    }
    
    @Override
    public void keyTyped(KeyEvent e) 
    {
    	
    }
    /*************************************************************************/
}