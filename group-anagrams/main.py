#Solution with counting

from collections import defaultdict
def group_anagrams(words):
    anagrams = defaultdict(list)

    for word in words:
        ltr_count = [0] * 26
        for letter in word:
            ltr_count[ord(letter) - ord('a')] += 1
        anagrams[tuple(ltr_count)].append(word)
    return anagrams.values()


print(group_anagrams(["eat","tea","tan","ate","nat","bat"]))


# Solution with sorting:

# from collections import defaultdict
# def groupanagrams(words):
#     anagrams = defaultdict(list)
#     for word in words:
#         sorted_word = "".join(sorted(word))
#         anagrams[sorted_word].append(word)
#     return anagrams.values()
    

# print(groupanagrams(["eat","tea","tan","ate","nat","bat"]))

