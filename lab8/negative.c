#include <stdio.h>

void debug_int(int x) {
	printf("decimal value is %d\n", x);
	printf("hex value is %X\n", x);
	printf("Location of value is %X\n\n\n", &x);

	return;
}

int main(void) {
	unsigned int x = 15;
	debug_int(x);

	int y = -15;
	debug_int(y);

	unsigned int my_test = 2147483648;
	debug_int(my_test);
	//printf("unsigned value is %d\n", my_test); //why is this like this?
	return 0;
}
