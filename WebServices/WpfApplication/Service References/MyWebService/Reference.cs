﻿//------------------------------------------------------------------------------
// <auto-generated>
//     This code was generated by a tool.
//     Runtime Version:4.0.30319.42000
//
//     Changes to this file may cause incorrect behavior and will be lost if
//     the code is regenerated.
// </auto-generated>
//------------------------------------------------------------------------------

namespace WpfApplication.MyWebService {
    
    
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    [System.ServiceModel.ServiceContractAttribute(Namespace="http://localhost/webservice", ConfigurationName="MyWebService.WebServiceSoap")]
    public interface WebServiceSoap {
        
        // CODEGEN: Generating message contract since element name HelloWorldResult from namespace http://localhost/webservice is not marked nillable
        [System.ServiceModel.OperationContractAttribute(Action="http://localhost/webservice/HelloWorld", ReplyAction="*")]
        WpfApplication.MyWebService.HelloWorldResponse HelloWorld(WpfApplication.MyWebService.HelloWorldRequest request);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://localhost/webservice/HelloWorld", ReplyAction="*")]
        System.Threading.Tasks.Task<WpfApplication.MyWebService.HelloWorldResponse> HelloWorldAsync(WpfApplication.MyWebService.HelloWorldRequest request);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://localhost/webservice/AddNumbers", ReplyAction="*")]
        double AddNumbers(double number1, double number2);
        
        [System.ServiceModel.OperationContractAttribute(Action="http://localhost/webservice/AddNumbers", ReplyAction="*")]
        System.Threading.Tasks.Task<double> AddNumbersAsync(double number1, double number2);
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
    [System.ServiceModel.MessageContractAttribute(IsWrapped=false)]
    public partial class HelloWorldRequest {
        
        [System.ServiceModel.MessageBodyMemberAttribute(Name="HelloWorld", Namespace="http://localhost/webservice", Order=0)]
        public WpfApplication.MyWebService.HelloWorldRequestBody Body;
        
        public HelloWorldRequest() {
        }
        
        public HelloWorldRequest(WpfApplication.MyWebService.HelloWorldRequestBody Body) {
            this.Body = Body;
        }
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
    [System.Runtime.Serialization.DataContractAttribute()]
    public partial class HelloWorldRequestBody {
        
        public HelloWorldRequestBody() {
        }
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
    [System.ServiceModel.MessageContractAttribute(IsWrapped=false)]
    public partial class HelloWorldResponse {
        
        [System.ServiceModel.MessageBodyMemberAttribute(Name="HelloWorldResponse", Namespace="http://localhost/webservice", Order=0)]
        public WpfApplication.MyWebService.HelloWorldResponseBody Body;
        
        public HelloWorldResponse() {
        }
        
        public HelloWorldResponse(WpfApplication.MyWebService.HelloWorldResponseBody Body) {
            this.Body = Body;
        }
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
    [System.Runtime.Serialization.DataContractAttribute(Namespace="http://localhost/webservice")]
    public partial class HelloWorldResponseBody {
        
        [System.Runtime.Serialization.DataMemberAttribute(EmitDefaultValue=false, Order=0)]
        public string HelloWorldResult;
        
        public HelloWorldResponseBody() {
        }
        
        public HelloWorldResponseBody(string HelloWorldResult) {
            this.HelloWorldResult = HelloWorldResult;
        }
    }
    
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    public interface WebServiceSoapChannel : WpfApplication.MyWebService.WebServiceSoap, System.ServiceModel.IClientChannel {
    }
    
    [System.Diagnostics.DebuggerStepThroughAttribute()]
    [System.CodeDom.Compiler.GeneratedCodeAttribute("System.ServiceModel", "4.0.0.0")]
    public partial class WebServiceSoapClient : System.ServiceModel.ClientBase<WpfApplication.MyWebService.WebServiceSoap>, WpfApplication.MyWebService.WebServiceSoap {
        
        public WebServiceSoapClient() {
        }
        
        public WebServiceSoapClient(string endpointConfigurationName) : 
                base(endpointConfigurationName) {
        }
        
        public WebServiceSoapClient(string endpointConfigurationName, string remoteAddress) : 
                base(endpointConfigurationName, remoteAddress) {
        }
        
        public WebServiceSoapClient(string endpointConfigurationName, System.ServiceModel.EndpointAddress remoteAddress) : 
                base(endpointConfigurationName, remoteAddress) {
        }
        
        public WebServiceSoapClient(System.ServiceModel.Channels.Binding binding, System.ServiceModel.EndpointAddress remoteAddress) : 
                base(binding, remoteAddress) {
        }
        
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
        WpfApplication.MyWebService.HelloWorldResponse WpfApplication.MyWebService.WebServiceSoap.HelloWorld(WpfApplication.MyWebService.HelloWorldRequest request) {
            return base.Channel.HelloWorld(request);
        }
        
        public string HelloWorld() {
            WpfApplication.MyWebService.HelloWorldRequest inValue = new WpfApplication.MyWebService.HelloWorldRequest();
            inValue.Body = new WpfApplication.MyWebService.HelloWorldRequestBody();
            WpfApplication.MyWebService.HelloWorldResponse retVal = ((WpfApplication.MyWebService.WebServiceSoap)(this)).HelloWorld(inValue);
            return retVal.Body.HelloWorldResult;
        }
        
        [System.ComponentModel.EditorBrowsableAttribute(System.ComponentModel.EditorBrowsableState.Advanced)]
        System.Threading.Tasks.Task<WpfApplication.MyWebService.HelloWorldResponse> WpfApplication.MyWebService.WebServiceSoap.HelloWorldAsync(WpfApplication.MyWebService.HelloWorldRequest request) {
            return base.Channel.HelloWorldAsync(request);
        }
        
        public System.Threading.Tasks.Task<WpfApplication.MyWebService.HelloWorldResponse> HelloWorldAsync() {
            WpfApplication.MyWebService.HelloWorldRequest inValue = new WpfApplication.MyWebService.HelloWorldRequest();
            inValue.Body = new WpfApplication.MyWebService.HelloWorldRequestBody();
            return ((WpfApplication.MyWebService.WebServiceSoap)(this)).HelloWorldAsync(inValue);
        }
        
        public double AddNumbers(double number1, double number2) {
            return base.Channel.AddNumbers(number1, number2);
        }
        
        public System.Threading.Tasks.Task<double> AddNumbersAsync(double number1, double number2) {
            return base.Channel.AddNumbersAsync(number1, number2);
        }
    }
}
