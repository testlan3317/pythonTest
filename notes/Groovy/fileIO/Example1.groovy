import java.io.File
class Example{
    static void main(String[] args){
        new File("example.txt").eachLine {
            line -> println "line: $line";     // line is the variable
        }
    }
}
/* The method eachLine is in-built in the File class in Groovy
 *
 *
 *
 */
