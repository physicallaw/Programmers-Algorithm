#include <vector>

using namespace std;

int solution(int n, vector<int> lost, vector<int> reserve)
{
   int answer = 0;
   vector<int> v(n, 1);
   for (int i = 0; i < lost.size(); ++i)
      --v[lost[i] - 1];
   for (int i = 0; i < reserve.size(); ++i)
      ++v[reserve[i] - 1];
   if (v[0] == 2 and v[1] == 0)
      v[0] == 1, v[1] = 1;
   for (int i = 1; i < n - 1; ++i)
      if (v[i] == 2 and v[i - 1] == 0)
         v[i] = 1, v[i - 1] = 1;
      else if (v[i] == 2 and v[i + 1] == 0)
         v[i] = 1, v[i + 1] = 1;
   if (v[n - 1] == 2 and v[n - 2] == 0)
      v[n - 1] == 1, v[n - 2] = 1;
   for (int i = 0; i < n; ++i)
      if (v[i] > 0)
         ++answer;

   return answer;
}