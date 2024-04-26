def isPalindrome( x: int) -> bool:
    s = str(x)
    l = len(s)
    for i in range(0, int((l + 1) / 2)):
        if s[i] != s[l - i - 1]:
            return False
    return True

print(isPalindrome(212))