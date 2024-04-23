Console.Write("Enter Weight");
int weight = int.Parse(Console.ReadLine());
Console.Write("Enter Length");
int length = int.Parse(Console.ReadLine());
Console.Write("Enter Width");
int width = int.Parse(Console.ReadLine());
Console.Write("Enter Height");
int height = int.Parse(Console.ReadLine());

int volume = length * width * height;

if (weight > 27 && volume > 100_0000)
    Console.WriteLine("Package is too heavy and too large!");
else if (weight > 27)
    Console.WriteLine("Package is too heavy");
else if (volume > 100_000)
    Console.WriteLine("Package is too large");
else
    Console.WriteLine("Package is okay");

Console.ReadKey();
