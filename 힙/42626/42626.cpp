#include <queue>

using namespace std;

int solution(vector<int> scoville, int K)
{
   int answer = 0;
   priority_queue<int> q;
   for (int i = 0; i < scoville.size(); ++i)
      q.push(-scoville[i]);
   while (q.top() > -K)
   {
      if (q.size() == 1)
         return -1;
      ++answer;
      int temp = q.top();
      q.pop();
      temp += q.top() * 2;
      q.pop();
      q.push(temp);
   }
   return answer;
}