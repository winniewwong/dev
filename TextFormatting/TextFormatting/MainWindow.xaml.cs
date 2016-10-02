using System;
using System.Text.RegularExpressions;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;

namespace TextFormatting
{
    /// <summary>
    /// Interaction logic for MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();

            // Initialize data for the rich text box 
            richTextBox.Document.Blocks.Clear();
            richTextBox.Document.Blocks.Add(new Paragraph(new Run("@you #hello there #welcome to @ our\n#Þárţƴ\na b\n@ #\n@a #b \n#a @b \n@a ##b \n@#a #@b \n#a#b \na@b a#b \n@a@b \n@#a#@b \n#@a#@b \n@#@#a #@#@b \n@#@#a#@#@b")));

            FormatText();
        }

        /// <summary>
        /// Format text when key up event fires
        /// </summary>
        /// <param name="sender"></param>
        /// <param name="e"></param>
        private void richTextBox_KeyUp(object sender, KeyEventArgs e)
        {
            FormatText();   
        }

        /// <summary>
        /// Format text color based of the specified search criteria
        /// </summary>
        private void FormatText()
        {
            TextRange textRange = new TextRange(richTextBox.Document.ContentStart, richTextBox.Document.ContentEnd);
            string text = textRange.Text;

            // Default all text to black color
            FormatTextColor(richTextBox, 0, text.Length, Brushes.Black);
           
            // Regex for the text formatting
            // Please go to test Regex on this website
            // https://regex101.com/r/xW5pS7/1    
            string pattern1 = @"(?<![(\w+)#])[@]\w+(?![@])|(?<![\w+])[#]\w+(?![#])";
            MatchCollection matches = null;

            // Set the valid text to red color
            if (IsValidRegex(text, pattern1, ref matches))
            {
                foreach (Match match in matches)
                    FormatTextColor(richTextBox, match.Index, match.Length, Brushes.Red);
            }         
        }

        /// <summary>
        /// Validate Regex for the text formatting
        /// </summary>
        private bool IsValidRegex(string text, string pattern, ref MatchCollection matches)
        {
            RegexOptions options = RegexOptions.IgnoreCase | RegexOptions.IgnorePatternWhitespace;
            
            try
            {
                matches = Regex.Matches(text, pattern, options);            
            }
            catch (ArgumentException)
            {
                MessageBox.Show("Invalid Regex!", "Text Formatting");
                return false;
            }

            return true;
        }

        /// <summary>
        /// Find the end position of the text
        /// </summary>
        /// <param name="startPos">start position of text</param>
        /// <param name="length">length of characters to format</param>
        /// <returns></returns>
        private static TextPointer GetTextPointAt(TextPointer startPos, int length)
        {
            TextPointer endPos = startPos;
            int i = 0;

            while ((i < length) && (endPos != null))
            {
                if ((endPos.GetPointerContext(LogicalDirection.Backward) == TextPointerContext.Text) ||
                    (endPos.GetPointerContext(LogicalDirection.Backward) == TextPointerContext.None))
                    i++;

                if (endPos.GetPositionAtOffset(1, LogicalDirection.Forward) == null)
                    return endPos;

                endPos = endPos.GetPositionAtOffset(1, LogicalDirection.Forward);
            }

            return endPos;
        }

        /// <summary>
        /// Format the text color for a specific text range
        /// </summary>
        /// <param name="rtb"></param>
        /// <param name="startIndex"></param>
        /// <param name="length"></param>
        /// <param name="color"></param>
        private void FormatTextColor(RichTextBox rtb, int startIndex, int length, SolidColorBrush color)
        {         
            // Get text start position
            TextPointer start = rtb.Document.ContentStart;

            // Get begin and end positions
            TextPointer startPos = GetTextPointAt(start, startIndex);
            TextPointer endPos = GetTextPointAt(start, startIndex + length);

            // Get the text range
            TextRange textRange = new TextRange(startPos, endPos);

            // Set the text color 
            textRange.ApplyPropertyValue(TextElement.ForegroundProperty, color);
        }
    }
 }

