public class Lab2_5_2 {
    public static void main(String[] args) {
        int[][] c = {{1,2,3,},{4,5,6},{2,3,4}};
        int[][] d = {{1,2,3,},{4,5,6},{2,3,4}};
        int[][] matrix2 = {{0,0,0},{0,0,0},{0,0,0}};
        for (int i = 0; i < c.length; i++) {
            for (int j = 0; j < c[i].length; j++) {
                for(int k = 0; k < matrix2[i].length; k++){
                    matrix2[i][j] = c[i][k] * d[k][j];
                }
                System.out.print(matrix2[i][j] + " ");
            }
            System.out.println();
        }
    }
}

