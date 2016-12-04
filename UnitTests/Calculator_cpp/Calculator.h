#pragma once

#include <stdexcept>

class Calculator
{
public:
	static int Addition( int num1, int num2 )
	{
		return num1 + num2;
	}

	static int Subtraction( int num1, int num2 )
	{
		return num1 - num2;
	}

	static int Multiplication( int num1, int num2 )
	{
		return num1 * num2;
	}

	static double Division( int dividend, int divisor )
	{
		if ( divisor == 0 )
			throw std::exception( "divisor can't be 0!" );
			//throw std::invalid_argument( "divisor can't be 0!" );

		return dividend / divisor;
	}
};