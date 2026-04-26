from failure import compute_failure
from kmp import kmp_search


def show_failure(pattern):
    result = compute_failure(pattern)
    print(f"pattern : {list(pattern)}")
    print(f"failure : {result}")
    print()


def show_search(text, pattern):
    matches = kmp_search(text, pattern)
    print(f"text    : {text}")
    print(f"pattern : {pattern}")
    if matches:
        print(f"found at positions: {matches}")
    else:
        print("no matches found")
    print()


print("failure function")
show_failure("ABAB")
show_failure("AABAA")
show_failure("ABCABD")

print("KMP search")
show_search("AABABAB", "ABAB")
show_search("ABABAC", "ABABAC")
show_search("ABABC", "ABABA")
show_search("AABAACAADAABAABA", "AABA")
