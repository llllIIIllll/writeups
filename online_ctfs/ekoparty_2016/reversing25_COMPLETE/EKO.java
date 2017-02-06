public class EKO { 

	public EKO() {} 

	public static void main(String args[]) {
	
		int i = 0; 
		for(int j = 0; j < 1337; j++) 
			i += j; 


		String s = (new StringBuilder()).append("EKO{").append(i).append("}").toString(); 

		System.out.print(s);

	} 

}