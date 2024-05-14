import java.io.File

class Example{
    static void main(String[] args){
        def src = new File("example.txt");
        def dst = new File("example1.txt");
        dst << src.text
    }
}
