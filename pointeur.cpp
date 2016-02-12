#include <iostream>
#include <new>

using namespace std;

struct Option
{
	int value;
	bool has_value;
};

int get(Option * opt) {
	return if (opt->has_value)
	{
		return opt->value;
	} else {
		throw 0;
	}
}

bool is_some(Option * opt) {
	return opt->has_value;
}

Option * some(int val){
	Option * p = new Option;
	p->value = val;
	p->has_value = true;
	return p;
}

Option * none(){
	Option * p = new Option;
	p->has_value = false;

}

struct Coords
{
	int x;
	int y;
};

int f1() {
	return 12;
	// return -1;
}

Option* f2() {
	int value = 12;
	return some(12);
}


int main()
{
	/* code */
	return 0;
}