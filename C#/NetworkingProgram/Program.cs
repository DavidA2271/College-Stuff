

class Program
{


    static void Main(string[] args)
    {
        bool endApp = false;
        // Display title as the C# console calculator app.
        Console.WriteLine("Network Address Calculator\n");
        Console.WriteLine("------------------------\n");

        while (!endApp)
        {
            int[] ipAddress;
            int[] subnetMask;

            string ipAddressString = AskIP();
            while (!ProcessInput(ipAddressString, out ipAddress))
            {
                ipAddressString = AskIP();
            }

            string subnetMaskString = AskSubnet();
            while (!ProcessInput(subnetMaskString, out subnetMask) || !ValidateSubnet(subnetMask))
            {
                subnetMaskString = AskSubnet();
            }

            string netAddress = CalculateNetworkAddress(ipAddress, subnetMask);
            Console.WriteLine($"Your network address is: {netAddress}");

            Console.WriteLine("------------------------\n");

            Console.Write("Press 'n' and Enter to close the app, or press any other key and Enter to continue: ");
            if (Console.ReadLine() == "n") endApp = true;

            Console.WriteLine("\n");
        }
        return;
    }

    static string AskIP()
    {
        Console.Write("Type your IP Address, and then press Enter: ");
        return Console.ReadLine();
    }

    static string AskSubnet()
    {
        Console.Write("Type your subnet mask, and then press Enter: ");
        return Console.ReadLine();
    }

    static bool ProcessInput(string input, out int[] output)
    {
        string[] inputArray = input.Split(".");
        if (inputArray.Length != 4)
        {
            Console.WriteLine($"{input} is not a valid input.");
            output = new int[4] { 0,0,0,0 };
            return false;
        }

        int[] ints = new int[inputArray.Length];

        for (int i = 0; i < inputArray.Length; i++)
        {
            int num = 0;
            if (!int.TryParse(inputArray[i], out num))
            {
                Console.WriteLine($"{input} has invalid characters.");
                output = new int[4] { 0, 0, 0, 0 };
                return false;
            }
            if (num > 255)
            {
                Console.WriteLine($"{input} has number(s) over 255.");
                output = new int[4] { 0, 0, 0, 0 };
                return false;
            }
            ints[i] = num;
        }
        output = ints;
        return true;
    }

    static bool ValidateSubnet(int[] subnet)
    {
        foreach (int subnetInt in subnet)
        {
            if (!(subnetInt == 0 || subnetInt == 255))
                return false;
        }
        return true;
    }

    static string CalculateNetworkAddress(int[] ip, int[] subnet)
    {
        int[] netAddress = new int[4];

        for (int i = 0; i < ip.Length; i++)
        {
            int subnetMultiplier = subnet[i] / 255;
            int netNum = ip[i] * subnetMultiplier;
            netAddress[i] = netNum;
        }
        
        return string.Join(".", netAddress);
    }
}
