<<<<<<< HEAD
#Python Code
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        global_min = (arrays[0][0], 0)
        global_max = (arrays[0][-1], 0)

        prev_min = (arrays[1][0], 1)
        prev_max = (arrays[1][-1], 1)

        if prev_min < global_min:
            prev_min, global_min = global_min, prev_min

        if prev_max > global_max:
            prev_max, global_max = global_max, prev_max

        for idx, a in enumerate(arrays[2:]):
            if a[0] < global_min[0]:
                prev_min = global_min
                global_min = (a[0], idx+2)
            elif a[0] < prev_min[0]:
                prev_min = (a[0], idx+2)

            if a[-1] > global_max[0]:
                prev_max = global_max
                global_max = (a[-1], idx+2)
            elif a[-1] > prev_max[0]:
                prev_max = (a[-1], idx+2)

        if global_max[1] != global_min[1]:
            return global_max[0] - global_min[0]
        else:
            print(global_max[0], prev_min[0], prev_max[0], global_min[0])
=======
#Python Code
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        n = len(arrays)
        global_min = (arrays[0][0], 0)
        global_max = (arrays[0][-1], 0)

        prev_min = (arrays[1][0], 1)
        prev_max = (arrays[1][-1], 1)

        if prev_min < global_min:
            prev_min, global_min = global_min, prev_min

        if prev_max > global_max:
            prev_max, global_max = global_max, prev_max

        for idx, a in enumerate(arrays[2:]):
            if a[0] < global_min[0]:
                prev_min = global_min
                global_min = (a[0], idx+2)
            elif a[0] < prev_min[0]:
                prev_min = (a[0], idx+2)

            if a[-1] > global_max[0]:
                prev_max = global_max
                global_max = (a[-1], idx+2)
            elif a[-1] > prev_max[0]:
                prev_max = (a[-1], idx+2)

        if global_max[1] != global_min[1]:
            return global_max[0] - global_min[0]
        else:
            print(global_max[0], prev_min[0], prev_max[0], global_min[0])
>>>>>>> 53cbd46aa08ed51a116a277d334efcc0225e7e90
            return max(global_max[0] - prev_min[0], prev_max[0] - global_min[0])