public class muti{
    public static void main(String[] args) {
    System.out.println(" ");
    int[][] c = {{1,2,3},
    {4,5,6},
    {2,3,4}};
    int[][] d = {{1,2,3},
    {4,5,6},
    {2,3,4}};
    int[][] matrix2 = {{0,0,0},
    {0,0,0},
     {0,0,0}};
    matrix2[0][0] = c[0][0] * d[0][0]+ c[0][1] * d[1][0] + c[0][2] * d[2][0];
    matrix2[0][1] = c[0][0] * d[0][1]+ c[0][1] * d[1][1] + c[0][2] * d[2][1];
    matrix2[0][2] = c[0][0] * d[0][2]+ c[0][1] * d[1][2] + c[0][2] * d[2][2];
    matrix2[1][0] = c[1][0] * d[0][0]+ c[1][1] * d[1][0] + c[1][2] * d[2][0];
    matrix2[1][1] = c[1][0] * d[0][1]+ c[1][1] * d[1][1] + c[1][2] * d[2][1];
    matrix2[1][2] = c[1][0] * d[0][2]+ c[1][1] * d[1][2] + c[1][2] * d[2][2];
    matrix2[2][0] = c[2][0] * d[0][0]+ c[2][1] * d[1][0] + c[2][2] * d[2][0];
    matrix2[2][1] = c[2][0] * d[0][1]+ c[2][1] * d[1][1] + c[2][2] * d[2][1];
    matrix2[2][2] = c[2][0] * d[0][2]+ c[2][1] * d[1][2] + c[2][2] * d[2][2];
    System.out.println(matrix2[0][0] + " " + matrix2[0][1] + " " + matrix2[0][2]);
    System.out.println(matrix2[1][0] + " " + matrix2[1][1] + " " + matrix2[1][2]);
    System.out.println(matrix2[2][0] + " " + matrix2[2][1] + " " + matrix2[2][2]);
    } 
    }
    