import java.util.Random;

public class SimpleThreadsSolution {

    // Display a message, preceded by the name of the current thread
    static void threadMessage(String message) {
        String threadName = Thread.currentThread().getName();
        System.out.format("%s: %s%n", threadName, message);
    }

    private static class MessageLoop implements Runnable {
        public void run() {
            String importantInfo[] = {
                "First man eats an orange",
                "Second woman eats an orange",
                "Third boy eats an orange",
                "Forth girl will eat an orange too."
            };
            try {
                for (int i = 0; i < importantInfo.length; i++) {
                    Thread.sleep(4000);  // Pause for 4 seconds
                    threadMessage(importantInfo[i]); // Print a message
                }
            } catch (InterruptedException e) {
                threadMessage("I wasn't done!");
            }
        }
    }

    public static void main(String args[])
        throws InterruptedException {

        // Delay, in milliseconds before we interrupt MessageLoop
        // thread (default one min).
        long patience = 1000 * 24;
        //patience = 5000; // try changing patience to 5000 and see what happens

        // If command line argument present, gives patience in seconds.
        if (args.length > 0) {
            try {
                patience = Long.parseLong(args[0]) * 1000;
            } catch (NumberFormatException e) {
                System.err.println("Argument must be an integer.");
                System.exit(1);
            }
        }

        threadMessage("Starting MessageLoop thread");
        long startTime = System.currentTimeMillis();
        Thread t = new Thread(new MessageLoop());
        t.start();

        threadMessage("Waiting for MessageLoop thread to finish");
        // loop until MessageLoop thread exits
        
        int count = 1;
        while (t.isAlive()) {
            threadMessage("Still waiting... " + count++);
            // Wait maximum of 1 second for MessageLoop thread to finish.
            t.join(1000);

//            try {
//                Random r = new Random();
//                Thread.currentThread().sleep(r.nextInt() % 500);
//            } catch (Exception e) { }

            if ( (System.currentTimeMillis() - startTime > patience)
                  && t.isAlive() ) {
                threadMessage("Tired of waiting!");
                t.interrupt();
                // Shouldn't be long now
                // -- wait indefinitely
                t.join();
            }
        }
        threadMessage("Finally!");
    }
}