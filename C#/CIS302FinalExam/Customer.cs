using System;
using System.Collections.Generic;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading.Tasks;
using System.Xml.Linq;

namespace CIS302FinalExam
{
    public class Person
    {
        public string Name;
        public string Address;
        public string PhoneNumber;

        public Person(string name, string address, string phoneNumber)
        { 
            Name = name;
            Address = address;
            PhoneNumber = phoneNumber;
        }
    }

    public class Customer : Person
    {
        public int CustomerID;
        public bool OnMailingList;

        public Customer(string name, string address, string phoneNumber,
            int customerID, bool onMailingList) : base(name, address, phoneNumber)
        {            
            CustomerID = customerID;
            OnMailingList = onMailingList;
        }

        public PreferredCustomer UpgradeCustomer()
        {
            return new PreferredCustomer(this);
        }
    }

    public class  PreferredCustomer : Customer
    {
        int purchaseTotal = 0;
        public int PurchaseTotal
        {
            get
            {
                return purchaseTotal;
            }
            set
            {
                purchaseTotal = value;
                UpdateDiscount();
            }
        }
        public int Discount;

        public PreferredCustomer(string name, string address, string phoneNumber,
            int customerID, bool onMailingList) : base(name, address, phoneNumber, customerID, onMailingList)
        {
            purchaseTotal = 0;
            Discount = 0;
        }

        public PreferredCustomer(string name, string address, string phoneNumber,
            int customerID, bool onMailingList, int _purchaseTotal) : 
            base(name, address, phoneNumber, customerID, onMailingList)
        {
            purchaseTotal = _purchaseTotal;
            Discount = 0;
            UpdateDiscount();
        }

        public PreferredCustomer(Customer customer) :
            base(customer.Name, customer.Address, customer.PhoneNumber,
                customer.CustomerID, customer.OnMailingList) { }

        public void AddToPurchaseTotal(int amount)
        {
            purchaseTotal += amount;
        }

        public void RemoveFromPurchaseTotal(int amount)
        {
            purchaseTotal -= amount;
        }

        void UpdateDiscount()
        {
            switch (purchaseTotal)
            {
                case >= 2000:
                    Discount = 10;
                    break;
                case >= 1500:
                    Discount = 7;
                    break;
                case >= 1000:
                    Discount = 6;
                    break;
                case >= 500:
                    Discount = 5;
                    break;
                default:
                    Discount = 0;
                    break;
            }
        }
    }
}
