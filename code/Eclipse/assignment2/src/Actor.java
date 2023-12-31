import java.awt.Graphics2D;
import java.awt.Image;
import javax.swing.ImageIcon;
/*****************************************************************************
    // This part should not be modified
    * >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>*/
  
public class Actor {
	public double x;
	public double y;
        public int width;
	public int height;
        private String image;
        private Image i;
        public boolean gasOn;
        public boolean breakOn;
        public int coins = 0;

	public Actor(String img) {
            changeImage(img); 
	}
        
        public Actor(String img, double a, double b) {
            x = a;
            y = b;
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
		g.drawImage(i, (int)x, (int) y, null);
	}
}