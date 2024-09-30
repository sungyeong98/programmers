class Solution {
    public String solution(String my_string) {
        StringBuilder temp = new StringBuilder();
        for(char i:my_string.toCharArray()){
            if(!"aeiou".contains(String.valueOf(i))){
                temp.append(i);
            }
        }
        return temp.toString();
    }
}