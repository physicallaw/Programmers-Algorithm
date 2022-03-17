#include <algorithm>
#include <string>
#include <vector>

using namespace std;

bool solution(vector<string> phone_book)
{
   sort(phone_book.begin(), phone_book.end());
   for (int i = 0; i < phone_book.size(); ++i)
      for (int j = i + 1; j < phone_book.size(); ++j)
         if (phone_book[i].size() >= phone_book[j].size() or phone_book[i][0] != phone_book[j][0])
            break;
         else if (phone_book[i] == string(phone_book[j].begin(), phone_book[j].begin() + phone_book[i].size()))
            return false;
   return true;
}