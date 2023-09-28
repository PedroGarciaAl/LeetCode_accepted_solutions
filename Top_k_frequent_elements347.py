class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums.sort()
        valores = {}
        lista2 = []

        for n in nums:
            if n not in valores:
                valores[n] = 1
            else:
                valores[n] += 1

        for n in range(0, k):
            lista2.append(max(valores, key=valores.get))
            del valores[max(valores, key=valores.get)]

        return lista2
    