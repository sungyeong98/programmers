class Solution {
    public String[] solution(String[] strArr) {
        int n = strArr.length;
        String[] result = new String[n];
        
        for(int i=0; i<n; i++){
            StringBuilder sb = new StringBuilder();
            
            for(char c:strArr[i].toCharArray()){
                if(i%2==0){
                    sb.append(Character.toLowerCase(c));
                }
                else{
                    sb.append(Character.toUpperCase(c));
                }
            }
            result[i]=sb.toString();
        }
        return result;
    }
}