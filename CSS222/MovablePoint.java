// public class MovablePoint implements Movable{
//     //Private member variables
//     private int x, y; //(x,y) coordinates of the point
//     //constructor
//     public MovablePoint(int x, int y) {
//         this.x = x;
//         this.y = y;
//     }
//     public String toString() {
//         return "Point at (" + x + "," + y + ")";
//     }
//     //Implement abstract methods declared in the interface Movable
//     public void moveUp() {y--;}
//     public void moveDown() {y++;}
//     public void moveLeft() {x--;}
//     public void moveRight() {x++;}
        
// }

public class MovablePoint implements Movable {
    int x, y, xSpeed, ySpeed;
    public MovablePoint(int x, int y, int xSpeed, int ySpeed) {
        this.x = x;
        this.y = y;
        this.xSpeed = xSpeed;
        this.ySpeed = ySpeed;
    }
    public void moveUp() {
        y -= ySpeed;
    }
    public void moveDown() {
        y += ySpeed;
    }
    public void moveLeft() {
        x -= xSpeed;
    }
    public void moveRight() {
        x += xSpeed;
    }
}