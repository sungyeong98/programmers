import java.util.*;
class Solution {
    public int[] solution(int[] arr) {
        Stack<Integer> stack = new Stack<>();
        
        for(int i=0; i<arr.length; i++){
            if(stack.isEmpty()){
                stack.push(arr[i]);
                continue;
            }
            if(stack.peek()==arr[i]){
                stack.pop();
                continue;
            }
            
            stack.push(arr[i]);
        }
        
        if(stack.isEmpty()){
            return new int[]{-1};
        }
        
        int[] result = new int[stack.size()];
        for(int i=stack.size()-1; i>=0; i--){
            result[i]=stack.pop();
        }
        
        return result;
    }
}