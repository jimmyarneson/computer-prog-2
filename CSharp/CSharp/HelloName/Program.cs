Console.Write("Enter Your Name: ");
string name = Console.ReadLine();
Console.WriteLine("Hello, " + name);

Console.Write("Enter your age: ");
//int age = Convert.ToInt32(Console.ReadLine());
int age = int.Parse(Console.ReadLine());
Console.WriteLine("You are " + age + " years old!");


Console.ReadKey();