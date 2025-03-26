/**
 * This creates the buffer and the producer and consumer threads.
 *
 * Figure 6.14
 *
 * @author Gagne, Galvin, Silberschatz
 * Operating System Concepts with Java - Eighth Edition
 * Copyright John Wiley & Sons - 2010.
 */

import java.util.Date;

public class Factory
{
	public static void main(String args[]) {
		Buffer<Date> server = new BoundedBuffer<Date>();

		Semaphore s1 = new Semaphore(0);
		//Semaphore s2 = new Semaphore(1);
		
		// now create the producer and consumer threads
		Thread producerThread = new Thread(new Producer(s1, server));
		Thread consumerThread = new Thread(new Consumer(s1, server));
		
		producerThread.start();
		consumerThread.start();               
	}
}
