#include <stdio.h>

int isPrime(num) {
	int i;
	int flag = 1;
	for (i = 2; i <= num - 1; i++) {
		if (num % i == 0) {
			flag = 0;
			break;
		}
	}
	return flag;
}

int main(void) {
	int k;
	int sum;
	for (k = 2; k <= 1000; k++) {
		if (isPrime(k)) {
			sum += k;
		}
	}
	printf("the sum is: %d \n", sum);
}
