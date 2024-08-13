//example on jagged array using Parallel Arrays for Initialization
import java.util.stream.IntStream;

class Prog18 {
    public static void main(String[] args) {
        int[][] sal = new int[3][]; 
        sal[0] = new int[2];
        sal[1] = new int[5];
        sal[2] = new int[3];
        
        int[] keys = {10, 50, 80};
        IntStream.range(0, sal.length).forEach(i -> {
            IntStream.range(0, sal[i].length).forEach(j -> {
                sal[i][j] = keys[i] + j * 10;
            });
        });
        
        printMatrix(sal);
    }
    
    public static void printMatrix(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                System.out.print(matrix[i][j] + "	");
            }
            System.out.println();
        }
    }
}
