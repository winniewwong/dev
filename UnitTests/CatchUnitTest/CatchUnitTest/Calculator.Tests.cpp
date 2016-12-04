// CatchUnitTest.cpp : Defines the entry point for the console application.
//



#include "stdafx.h"

// Download catch.hpp from this link
// https://github.com/philsquared/Catch

// Add reference: calculator project
// Properties->Include directories-> Calculator folder


#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"	

#include "Calculator.h"

#include <stdexcept>

TEST_CASE( "Addition", "Valid Addition" ) {
	REQUIRE( Calculator::Addition( 1, 2 ) == 3 );
}


TEST_CASE( "Division Exception" ) {
	REQUIRE_THROWS( Calculator::Division( 1, 0 )  );
	//INFO( "Divsor 0!" );
		/*WARN
		FAIL
		CAPTURE*/
}

//TEST_CASE( "wrong params", "[tag]" ) {
//	SECTION( "wrong rate" ) {
//		try {
//			my_func( 1.1 );  // must be in range [0..1]
//			REQUIRE_FALSE( "must raise issue about rate" );
//		}
//		catch ( const std::invalid_argument& e ) {
//			std::string str( e.what() );
//			std::string str2( "rate" );
//			REQUIRE_FALSE( str.find( str2 ) == std::string::npos );
//		}
//	}
//}