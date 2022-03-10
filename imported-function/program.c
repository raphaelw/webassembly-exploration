// program.c

void js_number_printer(int number);

int add(int first, int second) {
    int result = first + second;
	
    js_number_printer(result);
    return result;
}