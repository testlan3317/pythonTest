class Example{
    int x;

    public int getX(){
        return x;
    }

    public void setX(int pX){
        x = pX
    }

    static void main(String[] args){
        Example ex = new Example();
        ex.setX(100);
        println(ex.getX());
    }
}
