class Solution {
    public int maxProduct(int n) {
        int f=0;
        int l=0;
        while(n>0){
            int dig=n%10;
            if (dig>=f){
                l=f;
                f=dig;}
            else if (dig>l){
                l=dig;}
            n=n/10;
        }
       return f*l; 
    }
}