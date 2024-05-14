/**
 * if you want to recursively display all of files in a directory and its
 * subdirectories, then you would use the "eachFileRecurse" function of the
 * File class
 */
 
import java.io.File

class Example{
    static void main(String[] args){
        new File("../../notes").eachFileRecurse(){
            file -> println file.getAbsolutePath()
        }
    }
}
 
