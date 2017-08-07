package perceptron;

import java.util.ArrayList;
import java.util.List;

public class Perceptron {
	private double bias;
	private double w1;
	private double w2;
	public Perceptron(){
		this(0,1,1);
	}
	
	
	public Perceptron(double b){
		this(b,1,1);
	}
	
	public Perceptron(double b, double w1, double w2){
		this.bias=b;
		this.w1=w1;
		this.w2=w2;
	}
	
	public double getBias(){
		return this.bias;
	}
	
	public double getW1(){
		return this.w1;
	}
	
	public double getW2(){
		return this.w2;
	}
	
	public double getOutput(double x1,double x2){
		//System.out.print("Suma: ");
		//double p = this.w1*x1+this.w2*x2;
		//System.out.print(p);
		//System.out.print("  Decision: ");
		//double p1 = this.w1*x1+this.w2*x2 + this.bias;
		//System.out.println(p1);
		if (this.w1*x1+this.w2*x2 + this.bias <= 0){
			//System.out.println("Salida: 0");
			return 0;
		}
		else{
			//System.out.println("Salida: 1");
			return 1;
		}
	}
	
	public double NAND(double x1, double x2){
		this.w1=-2;
		this.w2=-2;
		this.bias=3;
		return this.getOutput(x1, x2);
	}
	
	public double AND(double x1, double x2){
		this.w1=1;
		this.w2=1;
		this.bias=-1.5;
		return this.getOutput(x1, x2);
	}
	
	public double OR(double x1, double x2){
		this.w1=1;
		this.w2=1;
		this.bias=-0.5;
		return this.getOutput(x1, x2);
	}
	
	public double[] summingBit(double x1, double x2){
		
		double[] result=new double[2];
		
		double out=0;
		double carryOut=1;
		
		result[0]=out;
		result[1]=carryOut;
		return result; 
	}

}
