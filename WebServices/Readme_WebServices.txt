Create a Web Services on Microsoft Visual Studio:
Create a empty C# web application
Add a new item, Web Service
Add additional web methods
Modify WebService Namespace to  [WebService(Namespace = "http://localhost/webservice")]
Turn on IIS from Windows Features
Run without debug

Create a WPF client App:
Create a WPF window application
Add service reference,  http://localhost:65296/WebService.asmx?WSDL
Add the following code to MainWindow.xaml.cs:
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


Test Soap and REST on SoapUI:
Create a new Soap project, enter http://localhost:65296/WebService.asmx?WSDL
Create a new REST project, enter http://localhost:65296/WebService.asmx?op=AddNumbers