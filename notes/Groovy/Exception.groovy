class Example {
    static void main(String[] args){
        try {
            def arr = new int[3];
            arr[5] = 5;
        } catch(ArrayIndexOutOfBoundsException ex) {
            println(ex.toString());
            println(ex.getMessage());
            println(ex.getStackTrace());
        } catch(Exception ex) {
            println("Catching the exception");
        } finally {
            print("The final block");
        }
        println("let's move on after the exception");
    }
}


/**
 * public String getMessage() 
 * returns detailed message about the exception that has occurred.This message is initialized in the Throwable constructor
 * 
 * public Throwable getCause()
 * returns the cause of the exception as represented by a Throwable object
 *
 * public String toString()
 * returns the name of the class concatenated with the result of getMessage()
 *
 * public void printStackTrace()
 * prints the result of toString() along with the stack trace to System.err, the error output stream
 *
 * public StackTraceElememt [] getStackTrace()
 * returns an array containing each element on the stack trace.The element at index 0 represents the top of the call stack, and the last
 * element in the array represents the method at the bottom of the call stack
 *
 * public Throwable fillInStackTrace()
 * Fills the stack trace of this Throwable object with the current trace, adding to any previous information in the stack trace.
 */
