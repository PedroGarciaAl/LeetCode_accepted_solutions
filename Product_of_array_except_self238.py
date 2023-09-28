class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        lista = [1] * len(nums)
        aux = 1
        aux2 = 1

        for i in range(len(nums)):
            lista[i] *= aux
            aux *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            lista[i] *= aux2
            aux2 *= nums[i]

        return lista
