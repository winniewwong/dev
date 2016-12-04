using System;
using Microsoft.VisualStudio.TestTools.UnitTesting;

namespace MSTest
{
    [TestClass]
    public class UnitTest1
    {
        [TestMethod]
        public void Addition()
        {
            Assert.AreEqual(Calculation.Calculator.Addition(1, 2), 3);
        }
    }
}
