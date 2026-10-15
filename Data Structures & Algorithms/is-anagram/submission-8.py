class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        list1 = []
        list2 = []

        for letter in s:
            list1.append(letter)

        for letter in t:
            list2.append(letter)

        if Counter(list1) == Counter(list2):
            return True
        else:
            return False