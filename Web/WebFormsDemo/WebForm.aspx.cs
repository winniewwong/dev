using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;

public partial class WebForm : System.Web.UI.Page
{
    protected void Page_Load(object sender, EventArgs e)
    {
        // server side page object being loaded in the memory
        //if (IsPostBack)
        //{
        //    string name = TextBox1.Text;
        //    string type = DropDownList1.SelectedValue;
        //    string fileName = FileUpload1.FileName;

        //    // TODO: record in Db
        //    FileUpload1.SaveAs(Server.MapPath("~/Content/" + fileName)); 
        //    Feedback.Text = "Submission saved.";
        //    // Refrest content folder to see a new file

        //}
    }

    protected void Button1_Click(object sender, EventArgs e)
    {
        string name = TextBox1.Text;
        string type = DropDownList1.SelectedValue;
        string fileName = FileUpload1.FileName;

        // TODO: record in Db
        FileUpload1.SaveAs(Server.MapPath("~/Content/" + fileName));
        Feedback.Text = "Submission saved.";
        // Refrest content folder to see a new file
    }
}