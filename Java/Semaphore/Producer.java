/**
 * This is the producer thread for the bounded buffer problem.
 *
 * Figure 6.12
 *
 * @author Gagne, Galvin, Silberschatz
 * Operating System Concepts with Java - Eighth Edition
 * Copyright John Wiley & Sons - 2010.
 */


import java.util.*;

public class Producer implements Runnable
{
	private  Buffer<Date> buffer;
	Semaphore semaphore;
	
	public Producer(Semaphore s, Buffer<Date> buffer) {
		this.semaphore = s;
		this.buffer = buffer;
	}
	
	public void run()
	{
		Date message;
		
		while (true) {
			System.out.println("Producer napping");
			SleepUtilities.nap();
			
			// produce an item & enter it into the buffer
			message = new Date();      
			System.out.println("Producer produced " + message);
			
			semaphore.release();
			buffer.insert(message);
		}
	}
	
}
