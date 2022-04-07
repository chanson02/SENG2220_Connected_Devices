int adder(int x, int y) { return x + y; }

int main(void) {
	unsigned int reading1 = 15;
	int reading2 = reading1 << 1;
	//int reading2 = 120;
	adder(reading1, reading2);
	return 0;
}
