import java.io.File

class Example {
    static void main(String[] args){
        new File(".").eachFile(){
            file -> println file.getAbsolutePath()
        }
    }
}
