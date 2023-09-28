class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anteriores = defaultdict(list)
        aux1, aux2 = '', ''

        for palavra in strs:
            aux1 = sorted(palavra)
            for char in aux1:
                aux2 += char

            anteriores[aux2].append(palavra)
            aux1, aux2 = '', ''

        return anteriores.values()

# Solucao 2:
#
#class Solution:
#    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
#        anteriores = defaultdict(list)
#
#        for palavra in strs:
#            anteriores[str(sorted(palavra))].append(palavra)
#
#        return anteriores.values()
