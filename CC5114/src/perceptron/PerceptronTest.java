package perceptron;

import static org.junit.Assert.*;

import org.junit.Before;
import org.junit.Test;



public class PerceptronTest {

	
	private Perceptron p;
	
	@Before
	public void setUp() throws Exception {
		p = new Perceptron();
	}
	
	@Test
	public void basicTest() {
		Perceptron p1 = new Perceptron(5);
		Perceptron p2 = new Perceptron(-1,2,3);
		assertEquals(0,p.getBias(),0);
		assertEquals(-1,p2.getBias(),0);
		assertEquals(5,p1.getBias(),0);
		assertEquals(2,p2.getW1(),0);
		assertEquals(3,p2.getW2(),0);
		assertEquals(0,p2.getOutput(0,0),0);
		assertEquals(1,p2.getOutput(1,2),0);	
	}
	
	@Test
	public void LogicalTest() {
		assertEquals(1,p.NAND(0,0),0);
		assertEquals(0,p.NAND(1,1),0);
		assertEquals(1,p.NAND(1,0),0);
		assertEquals(1,p.NAND(0,1),0);
		
		assertEquals(0,p.AND(0,0),0);
		assertEquals(1,p.AND(1,1),0);
		assertEquals(0,p.AND(1,0),0);
		assertEquals(0,p.AND(0,1),0);
		
		assertEquals(0,p.OR(0,0),0);
		assertEquals(1,p.OR(1,1),0);
		assertEquals(1,p.OR(1,0),0);
		assertEquals(1,p.OR(0,1),0);
		
		
	}
	
	@Test
	public void SummingTest() {
		double[] result = p.summingBit(0, 0);
		assertEquals(0,result[0],0);
		assertEquals(1,result[1],0);
		//assertEquals(0,p.NAND(1,1),0);
		//assertEquals(1,p.NAND(1,0),0);
		//assertEquals(1,p.NAND(0,1),0);
		
		//assertEquals(0,p.AND(0,0),0);
		//assertEquals(1,p.AND(1,1),0);
		//assertEquals(0,p.AND(1,0),0);
		//assertEquals(0,p.AND(0,1),0);
		
		//assertEquals(0,p.OR(0,0),0);
		//assertEquals(1,p.OR(1,1),0);
		//assertEquals(1,p.OR(1,0),0);
		//assertEquals(1,p.OR(0,1),0);
		
		
	}
	

}
