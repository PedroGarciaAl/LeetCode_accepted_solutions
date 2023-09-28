class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        anteriores = {}
        diminuido = 0

        for posicao, valor in enumerate(nums):
            diminuido = target - valor
            if diminuido in anteriores:
                return [anteriores[diminuido], posicao]
            anteriores[valor] = posicao
        return