def solution(numbers):
    answer = ''
    numbers = list(map(str, numbers))
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] < numbers[j] + numbers[i]:
                numbers[i], numbers[j] = numbers[j], numbers[i]
    answer = ''.join(numbers)
    if answer[0] == '0':
        return '0'
    return answer