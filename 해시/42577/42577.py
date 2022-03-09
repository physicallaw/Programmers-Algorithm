def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)):
        for j in range(i + 1, len(phone_book)):
            if phone_book[i][0] != phone_book[j][0]:
                break
            if len(phone_book[i]) >= len(phone_book[j]):
                break
            if phone_book[i] == phone_book[j][:len(phone_book[i])]:
                return False            
    return True