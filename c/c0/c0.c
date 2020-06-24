#include <stdio.h>

int isPrime(int num) {
	int flag = 1;
	for (int i = 2; i <= num - 1; i++) {
		if (num % i == 0) {
			flag = 0;
			break;
		}
	}
	return flag;
}

int main(void) {
	int sum = 0;
	for (int k = 2; k <= 1000; k++) {
		if (isPrime(k)) {
			sum += k;
		}
	}
	printf("the sum is: %d \n", sum);
	return 0;
}
