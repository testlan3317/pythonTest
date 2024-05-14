import java.io.File

class Example {
    static void main(String[] args){
        new File(".", "testfile.txt").withWriter('utf-8'){
            writer -> writer.writeLine 'Hello World';
        }
    }
}
