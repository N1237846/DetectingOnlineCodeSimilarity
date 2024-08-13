//example on jagged array using Custom Functional Interface
@FunctionalInterface
interface MatrixInitializer {
    void initialize(int[][] matrix, int start);
}

class Prog18 {
    public static void main(String[] args) {
        int[][] sal = new int[3][]; 
        sal[0] = new int[2];
        sal[1] = new int[5];
        sal[2] = new int[3];
        
        MatrixInitializer initializer = (matrix, start) -> {
            int key = start;
            for (int i = 0; i < matrix.length; i++) {
                for (int j = 0; j < matrix[i].length; j++) {
                    matrix[i][j] = key;
                    key += 10;
                }
            }
        };
        
        initializer.initialize(sal, 10);
        printMatrix(sal);
    }
    
    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int val : row) {
                System.out.print(val + "	");
            }
            System.out.println();
        }
    }
}
