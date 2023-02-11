class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 투 포인터를 이용한 풀이
        nums.sort()
        results = []

        for i in range(len(nums)-2):
            # 중복된 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
                
            left = i+1
            right = len(nums)-1
            while left < right:
                # 포인터 이동
                if nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                else:
                    # 정답 추가
                    results.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        # 중복 값 건너뛰기
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1

        return results