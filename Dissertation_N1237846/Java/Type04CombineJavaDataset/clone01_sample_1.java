//example on jagged array using enhanced for loop
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
        
        for (int[] row : sal) {
            for (int val : row) {
                System.out.print(val + "	");
            }
            System.out.println();
        }
    }
}
