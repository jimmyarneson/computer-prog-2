Console.Write("Enter Num1: ");
int num1 = int.Parse(Console.ReadLine());
Console.Write("Enter Num2: ");
int num2 = int.Parse(Console.ReadLine());
Console.Write("Choose an option: add, sub, mul, or div: ");
string op = Console.ReadLine();
int result = 0;

if (op == "add") result =  add(num1, num2);
else if (op == "sub") result = sub(num1, num2);
else if (op == "mul") result = mul(num1, num2);
else if (op == "div") result = div(num1, num2);
Console.WriteLine("Result: " + result);
wait();

static void wait() {  //void means "return nothing"
    Console.ReadLine();
    // return;
}

static int add(int x, int y) {
    return x + y;
}

static int sub(int x, int y) {
    return x - y;
}

static int mul(int x, int y) {
    return x * y;
}

static int div(int x, int y) {
    return x / y;
}