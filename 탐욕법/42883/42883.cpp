#include <string>

using namespace std;

string solution(string number, int k)
{
   string answer = number;
   for (int i = 0; i < k; ++i)
      for (int j = 0; j < answer.size(); ++j)
         if (answer[j] < answer[j + 1])
         {
            answer = string(answer.begin(), answer.begin() + j) + string(answer.begin() + j + 1, answer.end());
            break;
         }
   return string(answer.begin(), answer.begin() + number.size() - k);
}