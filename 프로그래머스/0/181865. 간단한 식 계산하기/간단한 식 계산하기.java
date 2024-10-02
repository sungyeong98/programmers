class Solution {
    public int solution(String binomial) {
        String[] bi = binomial.split(" ");
        int num1 = Integer.valueOf(bi[0]);
        int num2 = Integer.valueOf(bi[2]);
        String op = bi[1];
        switch(op) {
            case "+":
                return num1+num2;
            case "-":  
                return num1-num2;
            case "*":   
                return num1*num2;
            default:    
                break;
        }
        return 0;
    }
}