import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.ImageIcon;

/*
 * We need to declare the Kart class here:
 * The Kart class should inherit from the Actor class.
 */


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