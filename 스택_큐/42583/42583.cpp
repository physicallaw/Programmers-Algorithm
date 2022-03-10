#include <vector>

using namespace std;

int solution(int bridge_length, int weight, vector<int> truck_weights)
{
   int cnt = 0, l = 0;
   vector<int> v(bridge_length,0);
   for (auto it = truck_weights.begin(); it != truck_weights.end(); ++it)
   {
      while (cnt - v[l] + *it > weight)
      {
         v.push_back(0);
         cnt -= v[l++];
      }
      v.push_back(*it);
      cnt += *it - v[l++];
   }
   return v.size();
}