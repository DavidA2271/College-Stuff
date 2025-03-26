using System.Diagnostics;

namespace Easy_Planning_Calendar
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            var a = new CustomMonthObject();
            Controls.Add(a);
        }
    }
}