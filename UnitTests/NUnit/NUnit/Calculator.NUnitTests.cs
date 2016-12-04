using System;
using NUnit.Framework;

// Download Nunit Framework 3.x and NUnit3 Test Adapter from NuGet Package Manager
// If the tests are not showing in the Test Explorer, 
// make sure test project properties->Build->Platform Target matches Test->Test Settings->Default Processor Architecture
namespace NUnit
{
    [TestFixture]
    public class NUnitTest
    {
        [Test]
        public void Addition()
        {
            int result = Calculation.Calculator.Addition(1, 2);
            Assert.AreEqual(result, 3);
        }
    }
}