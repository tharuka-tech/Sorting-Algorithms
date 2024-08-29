package hanoi;

public class TowerOfHanoi {

	 // Recursive method to solve Tower of Hanoi
    public static void hanoi(int n, char source, char auxiliary, char target) {
        if (n == 1) {
            System.out.println("Move disk 1 from " + source + " to " + target);
            return;
        }
        hanoi(n - 1, source, target, auxiliary);
        System.out.println("Move disk " + n + " from " + source + " to " + target);
        hanoi(n - 1, auxiliary, source, target);
    }
	
	
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
		 int n = 3; // Number of disks
	     hanoi(n, 'A', 'B', 'C');
		
	}

}
