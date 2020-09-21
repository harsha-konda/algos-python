# https://leetcode.com/problems/subarray-sums-divisible-by-k/
def subarraysDivByK(A: List[int], K: int) -> int:
    prefixSum = 0
    remain_map  = {0: 0}
    count = 0
    for a in A:
        prefixSum += a
        remain = prefixSum % K
        if remain == 0:
            count+=1

        if remain in remain_map:
            count+= remain_map[remain]
        else:
            remain_map[remain] = 0
        remain_map[remain] += 1 

    return count 


if name == '__main__':
    assert(subarraysDivByK([4,5,0,-2,-3,1],5) == 7)

            
        
        
