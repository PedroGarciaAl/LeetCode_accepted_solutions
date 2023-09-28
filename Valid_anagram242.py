class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lista1, lista2 = [], []

        for letra in s:
            lista1.append(letra)
        for letra in t:
            lista2.append(letra)

        lista1.sort()
        lista2.sort()

        if lista1 == lista2:
            return True
        return False


#Solucao 2:

#class Solution:
#    def isAnagram(self, s: str, t: str) -> bool:
#        return sorted(s) == sorted(t)
