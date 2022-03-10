// program.c

void external_number_printer(int number);

int add(int a, int b) {
    int result = a + b;
	
    external_number_printer(result);
    return result;
}