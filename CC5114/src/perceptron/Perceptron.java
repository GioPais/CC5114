package perceptron;

import java.util.ArrayList;
import java.util.List;

public class Perceptron {
	private double bias;
	private double w1;
	private double w2;
	public Perceptron(){
		this.bias=0;
	}
	
	
	public Perceptron(double b){
		this.bias=b;
		this.w1=1;
		this.w2=1;
	}
	
	public Perceptron(double b, double w1, double w2){
		this.bias=b;
		this.w1=w1;
		this.w2=w2;
	}
	
	public double getW1(){
		return this.w1;
	}
	
	public double getW2(){
		return this.w2;
	}
	
	public void setW1(double w1){
		this.w1=w1;
	}
	
	public void setW2(double w1){
		this.w1=w2;
	}
	
	
	public boolean getOutput(double x1,double x2){
		if (this.w1*x1+this.w2*x2 + this.bias <= 0){
			return false;
		}
		else{
			return true;
		}
	}
	
	public boolean NAND(double x1, double x2){
		this.w1=-2;
		this.w1=-2;
		this.bias=3;
		return this.getOutput(x1, x2);
	}
	
	public boolean AND(double x1, double x2){
		this.w1=1;
		this.w1=1;
		this.bias=-1.5;
		return this.getOutput(x1, x2);
	}
	
	public boolean OR(double x1, double x2){
		this.w1=1;
		this.w1=1;
		this.bias=-0.5;
		return this.getOutput(x1, x2);
	}

}
