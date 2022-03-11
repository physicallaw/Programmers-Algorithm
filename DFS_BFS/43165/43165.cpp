#include <queue>

using namespace std;

int solution(vector<int> numbers, int target)
{
   int answer = 0, n = numbers.size();
   queue<vector<int>> q;
   q.push({numbers[0], 1});
   q.push({-numbers[0], 1});
   while (!q.empty())
   {
      if (q.front()[1] == n)
         if (q.front()[0] == target)
            ++answer;
      else
      {
         int t = q.front()[0];
         q.push({t + numbers[q.front()[1]], q.front()[1] + 1});
         q.push({t - numbers[q.front()[1]], q.front()[1] + 1});
      }
      q.pop();
   }

   return answer;
}