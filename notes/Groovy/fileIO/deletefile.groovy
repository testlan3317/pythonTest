import java.io.File

class Example{
    static void main(String[] args){
        def file = new File('testfile.txt');
        file.delete()
    }
}
