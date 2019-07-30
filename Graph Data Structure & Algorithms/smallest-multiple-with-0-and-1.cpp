/*
You are given an integer N. You have to find smallest multiple of N which consists of digits 0 and 1 only. Since this multiple could be large, return it in form of a string.

Note:

Returned string should not contain leading zeroes.
For example,

For N = 55, 110 is smallest multiple consisting of digits 0 and 1.
For N = 2, 10 is the answer.
 */

/*
I did not pass this one with Python. So C++ instead.
 */

using namespace std;

string Solution::multiple(int A) {

    queue<int> q;

    q.push((1%A));
    vector<int> vis(A+1,-1);
    vis[1%A]=1;
    vector<pair<int,char>> par(A+1,{-1,'1'});
    while(!q.empty()){
       int tp = q.front();
        q.pop();

        if (tp==0) {
            string s="";

            s+=par[0].second;
            int p = par[0].first;
            while(p!=-1){
                s+=par[p].second;
                p = par[p].first;
            }
            reverse(s.begin(),s.end());

            return s;
        }

        int a1 = (tp*10)%A;
        int a2 = ((tp*10)%A+1)%A;
        if (vis[a1]==-1){
            q.push(a1);

            vis[a1] =1;
            par[a1] = {tp,'0'};
        }

        if(vis[a2]==-1){
            q.push(a2);

            vis[a2]=1;

            par[a2] = {tp,'1'};
        }
    }
}
