#include <algorithm>
#include <queue>

using namespace std;

int solution(vector<vector<int>> jobs)
{
   sort(jobs.begin(), jobs.end());
   int answer = 0, t = jobs[0][0], n = jobs.size();
   priority_queue<vector<int>> pq;
   queue<vector<int>> q;
   for (int i = 0; i < n; ++i)
      q.push(jobs[i]);
      
   while (!pq.empty() or !q.empty())
   {
      if (pq.empty() and t < q.front()[0])
         t = q.front()[0];
      while (!q.empty() and q.front()[0] <= t)
      {
         pq.push({-q.front()[1], q.front()[0]});
         q.pop();
      }
      t -= pq.top()[0];
      answer += t - pq.top()[1];
      pq.pop();
   }
      
   return answer/n;
}