//example on jagged array using Recursion
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
        
        printMatrix(sal, 0, 0);
    }
    
    public static void printMatrix(int[][] matrix, int i, int j) {
        if (i < matrix.length) {
            if (j < matrix[i].length) {
                System.out.print(matrix[i][j] + "	");
                printMatrix(matrix, i, j + 1);
            } else {
                System.out.println();
                printMatrix(matrix, i + 1, 0);
            }
        }
    }
}
