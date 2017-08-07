package perceptron;

import java.util.ArrayList;
import java.util.List;

public class Perceptron {
	private boolean output;
	private float bias;
	ArrayList<Float> inputs;
	ArrayList<Float> gains;
	public Perceptron(){
		this.inputs = new ArrayList<Float>();
		this.gains = new ArrayList<Float>();
		this.bias=0;
	}
	
	public Perceptron(float b){
		this.bias=b;
	}
	
	public boolean getOutput(){
		if (this.sum() + this.bias <= 0){
			return false;
		}
		else{
			return true;
		}
	}

	private float sum() {
		// TODO Auto-generated method stub
		return 0;
	}

}
