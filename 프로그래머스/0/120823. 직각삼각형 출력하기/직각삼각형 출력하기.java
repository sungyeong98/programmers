import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        int cnt=1;
        while(cnt<=n){
            String temp = "";
            while(temp.length()<cnt){
                temp+='*';
            }
            System.out.println(temp);
            cnt+=1;
        }
    }
}