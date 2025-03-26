namespace CIS302FinalExam
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        List<PreferredCustomer> Customers = new List<PreferredCustomer>()
        {
            new PreferredCustomer(
                    "David Argueta",
                    "3 Bird Boulevard",
                    "555-213-5496",
                    127,
                    true,
                    3000
                    ),
            new PreferredCustomer(
                    "Mark Smith",
                    "10 Lion Way",
                    "555-581-4584",
                    456,
                    false
                    ),
            new PreferredCustomer(
                    "Janet Wood",
                    "7 Fox Drive",
                    "555-584-6942",
                    108,
                    false,
                    500
                    ),
            new PreferredCustomer(
                    "Tyler Fernandes",
                    "21 Egg Avenue",
                    "555-846-3218",
                    273,
                    true
                    ),
            new PreferredCustomer(
                    "Casey Roberts",
                    "32 Platypus Circle",
                    "555-321-5876",
                    192,
                    true,
                    1627
                    )
        };

        int currentCustomer = 0;
        protected override void OnLoad(EventArgs e)
        {
            base.OnLoad(e);

            SetLabels();
        }

        void SetLabels()
        {
            if (Customers == null || Customers.Count <= 0) return;
            var customer = Customers[currentCustomer];
            nameLabel.Text = customer.Name;
            addressLabel.Text = customer.Address;
            phnLabel.Text = customer.PhoneNumber;
            customeridLabel.Text = customer.CustomerID.ToString();
            mailingLabel.Text = customer.OnMailingList ? "Yes" : "No";
            pTotalLabel.Text = customer.PurchaseTotal.ToString();
            discountLabel.Text = customer.Discount.ToString();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            int prevIndex = currentCustomer;
            currentCustomer = Math.Clamp(currentCustomer - 1, 0, Customers.Count - 1);
            if (prevIndex != currentCustomer) SetLabels();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            int prevIndex = currentCustomer;
            currentCustomer = Math.Clamp(currentCustomer + 1, 0, Customers.Count - 1);
            if (prevIndex != currentCustomer) SetLabels();
        }
    }
}