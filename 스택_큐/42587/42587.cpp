#include <queue>

using namespace std;

int solution(vector<int> priorities, int location)
{
   int answer = 1;
   priority_queue<int> pq;
   queue<vector<int>> q;

   for (int i = 0; i < priorities.size(); ++i)
   {
      pq.push(priorities[i]);
      q.push({priorities[i], i});
   }
   while (q.front()[0] != pq.top() or q.front()[1] != location)
   {
      if (q.front()[0] == pq.top())
      {
         pq.pop();
         ++answer;
      }
      else
         q.push(q.front());
      q.pop();
   }

   return answer;
}