class Solution {
    public int solution(int a, int b) {
        int v1 = Integer.parseInt(String.valueOf(a)+String.valueOf(b));
        int v2 = 2*a*b;
        return v1>v2?v1:v2;
    }
}