#include "stdafx.h"
#include "CppUnitTest.h"
#include "Calculator.h"
#include <functional>

// VS2015 Native Unit Test
// Add Calculator project path
using namespace Microsoft::VisualStudio::CppUnitTestFramework;

namespace NativeUnitTest
{
	TEST_CLASS( UnitTest1 )
	{
	public:

		TEST_METHOD( Addition )
		{
			int result = Calculator::Addition( 1, 2 );
			Assert::AreEqual( result, 3 );
		}

		TEST_METHOD( Subtraction )
		{
			int result = Calculator::Subtraction( 10, 2 );
			Assert::AreEqual( result, 8 );
		}

		TEST_METHOD( Multiplication )
		{
			int result = Calculator::Multiplication( 100, 2 );
			Assert::AreEqual( result, 200 );
		}


		TEST_METHOD( Division )
		{
			double result = Calculator::Division( 100, 2 );
			Assert::AreEqual( result, 50.0 );
		}

		TEST_METHOD( DivisionTryCatch )
		{
			bool exceptionThrown = false;

			try
			{
				double result = Calculator::Division( 100, 0 );
			}
			catch ( std::exception& ex )
			{
				auto messgae = ex.what();
				exceptionThrown = true;
			}

			Assert::IsTrue( exceptionThrown );
		}

		TEST_METHOD( DivisionExpectException )
		{
			//std::function<double( void )> act = [] { return Calculator::Division( 1, 0 ); };
			//Assert::ExpectException<std::invalid_argument>( act );

			auto act = [] {  Calculator::Division( 1, 0 ); };
			Assert::ExpectException<std::exception>( act );
		}
	};
}