package week2;

public class BooleanExpr {
	public static void main(String[] args) {
		boolean a = Boolean.parseBoolean(args[0]);
		boolean b = Boolean.parseBoolean(args[1]);
		
		boolean phi = (!(a && b ) && (a || b )) || ((a && b) || !(a || b));
		
		System.out.print("a: " + a + "\nb: " + b + "\nphi: " + phi + "\n");
	}
}
