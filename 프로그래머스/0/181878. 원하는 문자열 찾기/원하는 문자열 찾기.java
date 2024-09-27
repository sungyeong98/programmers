class Solution {
    public int solution(String myString, String pat) {
        String new_string = "";
        String new_pat = "";
        for(char i:myString.toCharArray()){
            new_string+=Character.toLowerCase(i);
        }
        for(char i:pat.toCharArray()){
            new_pat+=Character.toLowerCase(i);
        }
        return new_string.contains(new_pat)?1:0;
    }
}