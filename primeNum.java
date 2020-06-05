package primeNum;
import java.util.ArrayList;
public class primeNum {
	public static ArrayList<Integer> primeList;
	public primeNum(){
		primeList= new ArrayList<Integer>();
	}
	public static boolean notDivBefore(int current) {
		if(primeList!=null) {
			for(int b:primeList) {
				if(current%b==0) {
					return false;
				}
			}
			return true;
		}
		else {
			return true;
		}
		
	}
	public static void getPrime() {
		primeList.add(2);
		for(int num=2;num<=100000;num++) {
			for(int k=2;k<=Math.sqrt(num);k++) {
				if(notDivBefore(num)) {
					//System.out.println("once");
					//System.out.println("here111");
					//System.out.println(num);
					primeList.add(num);
					//System.out.println("here");
				}
			}
		}
		
	}
	public static void main(String[] args) {
		primeNum prime=new primeNum();
		long start=System.currentTimeMillis();
		getPrime();
		int sum=0;
		for(int i=0;i<primeList.size();i++) {
			sum+=primeList.get(i);
		}
		System.out.println("The sum of the prime numbers in 100000(included) is: "+sum);
		long end=System.currentTimeMillis();
		System.out.println("the running time of this code is: "+(end-start)+"ms");
	}
	
}
