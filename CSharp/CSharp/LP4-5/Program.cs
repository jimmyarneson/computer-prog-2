Console.WriteLine("Enter Your Grade Percent ");
double grade = double.Parse(Console.ReadLine());
char letgrade = ' ';
if (grade >= 90)
    letgrade = 'A';
else if (grade >= 80)
    letgrade = 'B';
else if (grade >= 70)
    letgrade = 'c';
else if (grade >= 60)
    letgrade = 'd';
else
    letgrade = 'f';

Console.WriteLine("The corresponding letter grade is: " + letgrade);
Console.ReadKey();