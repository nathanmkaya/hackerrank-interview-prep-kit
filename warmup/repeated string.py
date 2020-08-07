def repeatedString(s, n):
    if s == "a":
        return n
    # repetitions = n % len(s) + (n - n % len(s)) / len(s)
    # string = s * int(repetitions)
    # count = len([i for i in string[:n] if i == "a"])
    # return count
    full_repetitions = int(n/len(s))
    partial_repetition = int(n % len(s))
    full_count = len([i for i in s if i == "a"])
    partial_count = len([i for i in s[:partial_repetition] if i == "a"])
    return full_count*full_repetitions+partial_count



if __name__ == "__main__":
    print(repeatedString("aba", 10))
    print(repeatedString("a", 1000000000000))
