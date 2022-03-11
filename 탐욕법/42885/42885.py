def solution(people, limit):
    answer = 0
    people.sort()
    l, r = 0, len(people) - 1
    while l <= r:
        temp = people[r]
        r -= 1
        while temp + people[l] <= limit:
            temp += people[l]
            l += 1
        answer += 1
    return answer