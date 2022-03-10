#include <stack>
#include <vector>

using namespace std;

vector<int> solution(vector<int> prices)
{
   vector<int> answer(1, 0);
   int n = prices.size();
   stack<int> s;
   s.push(prices[n - 1]);
   for (int i = n - 2; i >= 0; --i)
   {
      int temp = 0;
      while (!s.empty())
      {
         if (prices[i] > s.top())
            break;
         ++temp;
         s.pop();
      }
      answer.push_back(temp + (s.empty() ? 0 : 1));
      for (int j = i + temp; j >= i; --j)
         s.push(prices[j]);
   }

   return vector<int>(answer.rbegin(), answer.rend());
}