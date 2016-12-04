using System;
using System.Linq;
using Xunit;


// Add References: Calculator project
// Make sure Test/Test Settings/Default Processor Architecture is set to the same as build platform target 
// in order for the Test Explorer to detect the tests
namespace xUnitTest
{
    public class UnitTest
    {
        [Fact]
        public void Addition()
        {
            int result = Calculation.Calculator.Addition(1, 2);
            Assert.Equal(result, 3);
        }
    }
}
