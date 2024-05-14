import java.io.File

class Example{
    static void main(String[] args){
        File file = new File("example.txt")
        println "The file ${file.absolutePath} has ${file.length()} bytes"
    }
}
/**
 * ${file.absolutePath}
 * ${file.length()}
 */
