using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;

namespace WpfApplication
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            MyWebService.WebServiceSoapClient client = new MyWebService.WebServiceSoapClient();

            string helloString = client.HelloWorld();
            output.Content = helloString;
        }

        private void button_Click(object sender, RoutedEventArgs e)
        {

            double value1 = Convert.ToDouble(input1.Text);
            double value2 = Convert.ToDouble(input2.Text);
            MyWebService.WebServiceSoapClient client = new MyWebService.WebServiceSoapClient();

            double result = client.AddNumbers(value1, value2);
            output.Content = result.ToString();
        }
    }
}
