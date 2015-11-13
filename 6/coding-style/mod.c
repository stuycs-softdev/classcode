/*------------------------------ mod.c ------------------------------*/
/*
	description of the file

	void f1(int x) -- brief description of function f1
	
	int f2(int a, int b) - brief description of f2
*/

/*------------------------------ includes ------------------------------*/

#include <stdio.h>
#include <stdlib.h>
#include "mystuff.h"

/*------------------------------ defines / globals------------------------------*/

#define MYVAL 1

int a;

/*------------------------------ Structs / typedefs ------------------------------*/
struct s1 {
	int a;
	char b;
};

/*------------------------------ functions ------------------------------*/
/*=======================================================================*/
/*=======================================================================*/



/*------------------------------ f1 ------------------------------*/

/*
	Does something cool to the parameter x

	params: x - an integer

	returns: void

	MZ timestamp
	MZ newtimestamp
	MZ newtimestamp
*/
void function f1(int x){
	/* doing someting */
}

/*------------------------------ f2 ------------------------------*/
/*
	Does something cool to the parameter x

	params: a - an integer
	b - an integer

	returns: the sum of a+b

	MZ timestamp
*/
int function f2(int a, int b){
	return a+b;
}
