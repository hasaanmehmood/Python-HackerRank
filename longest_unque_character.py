def longest_unique_substring(s: str, k: int) -> str:
    left = 0
    seen = set()
    best = ""

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        # Update answer only if length >= k
        if right - left + 1 >= k and (right - left + 1) > len(best):
            best = s[left:right + 1]

    return best
print(longest_unique_substring("abcabcbb", 3))  # Output: "abc"
print(longest_unique_substring("bbbbb", 2))     # Output: " "    