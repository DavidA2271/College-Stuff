/**
 * This is the consumer thread for the bounded buffer problem.
 *
 * Figure 6.13
 *
 * @author Gagne, Galvin, Silberschatz
 * Operating System Concepts with Java - Eighth Edition
 * Copyright John Wiley & Sons - 2010.
 */

import java.util.*;

public class Consumer implements Runnable
{
	private  Buffer<Date> buffer;
    Semaphore semaphore;

   public Consumer(Semaphore s, Buffer<Date> buffer) { 
      this.semaphore = s;
      this.buffer = buffer;
   }
   
   public void run()
   {
      Date message;
   
     while (true)
      {
         System.out.println("Consumer napping");
	      SleepUtilities.nap(); 
         
         // consume an item from the buffer
         System.out.println("Consumer wants to consume.");
           
         semaphore.acquire();
         message = buffer.remove();
      }
   }
   
}


