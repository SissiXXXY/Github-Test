package primeNum;
import java.math.BigInteger;
import java.util.ArrayList;
public class fibo1000 { 
	public static void main(String[] args) {
		ArrayList<BigInteger> fiboList=new ArrayList<BigInteger>();
		fiboList.add(BigInteger.ONE);
		fiboList.add(BigInteger.TWO);
		//System.out.println(fiboList.size());
		while(true){
			BigInteger next=fiboList.get(fiboList.size()-1).add(fiboList.get(fiboList.size()-2));
			if(fiboList.size()>1000) {
				break;
			}
			else {
				fiboList.add(next);
			}
		}
		System.out.println(fiboList.get(1000));
	}
}
