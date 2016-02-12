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

Option * Some(int val){
	Option * p = new Option;
	p->value = val;
	p->has_value = true;
	return p;
}

Option * None(){
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
	//int value = 12;
	//return Some(12);
	return None();
}

template<class T>
T mul (T a, T b) {
	return a*b;
}


int main()
{
	int i = mul(2,3);
	double f = mul(2.2,5.3);
	return 0;
}