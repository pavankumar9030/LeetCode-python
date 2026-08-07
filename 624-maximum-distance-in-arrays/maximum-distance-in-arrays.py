class Solution:
    def maxDistance(self, arrays):

        minimum = arrays[0][0]
        maximum = arrays[0][-1]
        answer = 0

        for i in range(1, len(arrays)):

            answer = max(answer,
                         arrays[i][-1] - minimum,
                         maximum - arrays[i][0])

            minimum = min(minimum, arrays[i][0])
            maximum = max(maximum, arrays[i][-1])

        return answer