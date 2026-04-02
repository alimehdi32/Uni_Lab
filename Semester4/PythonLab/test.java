import java.util.*;
public class test {
    public static int isCyclicRotation(String p, String q)  {
        if(p.length()==0) return 0;
        if(p.equals(q)) return 1;
        // String str=p;
        // int len = p.length();
        // int start=p.length()-1;
        // int rotations=0;
        // while(rotations<len){
        //     char c=p.charAt(start);
        //     str=c+str;
        //     if(q.equals(str.substring(0,len))) return 1;
        //     else{
        //         start--;
        //         rotations++;
        //     }
        // }
        // return 0;
        int start=1;
        int end=p.length()-1;
        while(start<q.length() && end>0){
            if(p.substring(0,end).equals(q.substring(start,q.length()))) return 1;
            else{
                start++;
                end--;
            }
        }
        return 0;
    }
    public static void main(String args[]){
        test obj = new test();
        System.out.println(obj.isCyclicRotation("aabca", "bacaa"));
    }
}