class Solution {
    public int solution(int a, int b) {
        if(a%2==1 && b%2==1){
            return (int)((double)Math.pow(a,2)+(double)Math.pow(b,2));
        }
        else if(a%2==1 || b%2==1){
            return 2*(a+b);
        }
        else{
            return a>b?a-b:b-a;
        }
    }
}