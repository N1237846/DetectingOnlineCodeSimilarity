//example on jagged array using Builder Pattern
class MatrixBuilder {
    private int[][] matrix;
    private int start;
    
    public MatrixBuilder(int rows) {
        matrix = new int[rows][];
    }
    
    public MatrixBuilder addRow(int rowIndex, int columns) {
        matrix[rowIndex] = new int[columns];
        return this;
    }
    
    public MatrixBuilder initialize(int start) {
        this.start = start;
        return this;
    }
    
    public int[][] build() {
        int key = start;
        for (int i = 0; i < matrix.length; i++) {
            for (int j = 0; j < matrix[i].length; j++) {
                matrix[i][j] = key;
                key += 10;
            }
        }
        return matrix;
    }
}

class Prog18 {
    public static void main(String[] args) {
        int[][] sal = new MatrixBuilder(3)
            .addRow(0, 2)
            .addRow(1, 5)
            .addRow(2, 3)
            .initialize(10)
            .build();
        
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
