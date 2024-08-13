//example on jagged array using Functional Interface and Lambda Expression
import java.util.function.BiConsumer;

class Prog18 {
    public static void main(String[] args) {
        int[][] sal = new int[3][]; 
        sal[0] = new int[2];
        sal[1] = new int[5];
        sal[2] = new int[3];
        
        int key = 10;
        for (int i = 0; i < sal.length; i++) {
            for (int j = 0; j < sal[i].length; j++) {
                sal[i][j] = key;
                key += 10;
            }
        }
        
        BiConsumer<int[][], Integer> displayMatrix = (matrix, n) -> {
            for (int[] row : matrix) {
                for (int val : row) {
                    System.out.print(val + "	");
                }
                System.out.println();
            }
        };
        
        displayMatrix.accept(sal, 2);
    }
}
