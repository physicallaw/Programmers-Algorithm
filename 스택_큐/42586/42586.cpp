#include <queue>

using namespace std;

vector<int> solution(vector<int> progresses, vector<int> speeds)
{
   vector<int> answer;
   int n = speeds.size();
   queue<int> q;
   for (int i = 0; i < n; ++i)
      q.push((100 - progresses[i]) / speeds[i] + ((100 - progresses[i]) % speeds[i] ? 1 : 0));
   int m = q.front(), temp = 0;
   while (!q.empty())
   {
      if (q.front() <= m)
         ++temp;
      else
      {
         answer.push_back(temp);
         temp = 1;
         m = q.front();
      }
      q.pop();
   }
   answer.push_back(temp);

   return answer;
}