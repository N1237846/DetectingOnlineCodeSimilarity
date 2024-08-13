//example on jagged array using Loop Unrolling
class Prog18 {
    public static void main(String[] args) {
        int[][] sal = new int[3][]; 
        sal[0] = new int[2];
        sal[1] = new int[5];
        sal[2] = new int[3];
        
        int key = 10;
        sal[0][0] = key; key += 10;
        sal[0][1] = key; key += 10;
        
        sal[1][0] = key; key += 10;
        sal[1][1] = key; key += 10;
        sal[1][2] = key; key += 10;
        sal[1][3] = key; key += 10;
        sal[1][4] = key; key += 10;
        
        sal[2][0] = key; key += 10;
        sal[2][1] = key; key += 10;
        sal[2][2] = key; key += 10;
        
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
