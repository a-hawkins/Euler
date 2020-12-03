// PE 11 v1
// 12-3-2020

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

public class pe_11_v1 
{
	public static void printArray(int [][] a)
	// TASK: prints out a 2D array to the console
	// Intended for debugging
	{
		for(int i = 0; i < a.length; i++)
		{
			for(int j = 0; j < a[i].length; j++) {
				System.out.print(a[i][j] + " ");
			}
			System.out.println();
		}
	}
	
	public static void checkSizes() 
	//TASK: Print out the max value of some primitive data types
	//		As well as the max value of a product of 4 2-digit numbers
	/* Results: 
	 * Max Product: 96059601
	 * Max Integer: 2147483647
	 * Max Long: 9223372036854775807
	 * 
	 * int should be big enough for these products
	 */
	{
		System.out.println("Max Product: " + (long)Math.pow(99, 4));
		System.out.println("Max Integer: " + Integer.MAX_VALUE);
		System.out.println("Max Long: " + Long.MAX_VALUE);
	}
	
	public static int horiProd(int [][] a)
	{
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < a.length; i++)
		{
			for(int j = 0; j < a.length-3; j++)
			{
				int prod = a[i][j] * a[i][j+1] * a[i][j+2] * a[i][j+3];
				if (prod > max)
					max = prod;
			}
		}
		return max;
	}
	
	public static int vertProd(int [][] a)
	{
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < a.length-3; i++)
		{
			for(int j = 0; j < a.length; j++)
			{
				int prod = a[i][j] * a[i+1][j] * a[i+2][j] * a[i+3][j];
				if (prod > max)
					max = prod;
			}
		}
		return max;
	}
	
	public static int diagRightProd(int [][] a)
	{
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < a.length-3; i++)
		{
			for(int j = 0; j < a.length-3; j++)
			{
				int prod = a[i][j] * a[i+1][j+1] * a[i+2][j+2] * a[i+3][j+3];
				if (prod > max)
					max = prod;
			}
		}
		return max;
	}
	
	public static int diagLeftProd(int [][] a)
	{
		int max = Integer.MIN_VALUE;
		for(int i = 3; i < a.length; i++)
		{
			for(int j = 0; j < a.length-3; j++)
			{
				int prod = a[i][j] * a[i-1][j+1] * a[i-2][j+2] * a[i-3][j+3];
				if (prod > max)
					max = prod;
			}
		}
		return max;
	}
	
	public static int maxValue (int [] a)
	{
		int max = Integer.MIN_VALUE;
		for(int i = 0; i < a.length; i++)
		{
			if (a[i] > max)
				max = a[i];
		}
		return max;
	}

	public static void main(String [] args) throws FileNotFoundException
	{
		boolean debugMode = false;
		
		Scanner scan = new Scanner(new File("input.txt"));
		
		//read in grid from text file to int [20][20] grid
		int [][] grid = new int[20][20];
		for(int i = 0; i < 20; i++)
		{
			String line = scan.nextLine();
			Scanner lineScan = new Scanner(line);
			for(int j = 0; j < 20; j++)
			{
				grid[i][j] = lineScan.nextInt();
			}//end for(int j = 0; j < 20; i++) {
			
		}//end for(int i = 0; i < 20; i++) {
		
		if (debugMode)
		{
			checkSizes();
			printArray(grid);
			
			System.out.println(horiProd(grid));
			System.out.println(vertProd(grid));
			System.out.println(diagRightProd(grid));
			System.out.println(diagLeftProd(grid));
		}//end if(debugMode);
		
		int [] results = {horiProd(grid), vertProd(grid), diagRightProd(grid), diagLeftProd(grid)};
		
		System.out.println(maxValue(results));
	}//end public static void main(String [] args) ... {

}//end public class PE11 {
