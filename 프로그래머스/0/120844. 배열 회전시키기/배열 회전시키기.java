class Solution {
    public int[] solution(int[] numbers, String direction) {
        int[] result = new int[numbers.length];
        
        if(direction.equals("left")){
            for(int i=0; i<numbers.length; i++){
                result[i] = numbers[(i+1) % numbers.length];
            }
        }
        else if(direction.equals("right")){
            for(int i=0; i<numbers.length; i++){
                result[i] = numbers[(i-1+numbers.length)%numbers.length];
            }
        }
        return result;
    }
}