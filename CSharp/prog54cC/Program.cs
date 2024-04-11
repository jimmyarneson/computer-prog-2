/*
 * Created by SharpDevelop.
 * User: arneson.j1
 * Date: 4/11/2024
 * Time: 2:05 PM
 * 
 * To change this template use Tools | Options | Coding | Edit Standard Headers.
 */
using System;

namespace prog54cC
{
	class Program
	{
		public static void Main(string[] args)
		{
			Console.Write("Enter Radius: ");
			double rad = double.Parse(Console.ReadLine());
			double Pi = 3.14159;
			
			double area = Pi * rad * rad ;
			double circ = Pi * rad * 2;
			
			Console.WriteLine("Area: " + Math.Round(area, 3));
			Console.WriteLine("Circumfrence: " + Math.Round(circ, 3));
			Console.ReadKey();
		}
	}
}