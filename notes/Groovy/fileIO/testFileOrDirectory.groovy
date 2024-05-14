import java.io.File

class Example {
    static void main(String[] args){
        def file = new File('.')
        println "File? ${file.isFile()}"
        println "Directory? ${file.isDirectory()}"
    }
}
