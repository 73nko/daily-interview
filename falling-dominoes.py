###
# 05-12-2020
# Hi, here's your problem today. This problem was recently asked by Twitter:

# Given a string with the initial condition of dominoes, where:

# . represents that the domino is standing still
# L represents that the domino is falling to the left side
# R represents that the domino is falling to the right side

# Figure out the final position of the dominoes. If there are dominoes that get pushed on both ends, the force cancels out and that domino remains upright.
###
class Solution(object):
    def pushDominoes(self, dominoes):
        N = len(dominoes)
        force = [0] * N

        # Populate forces going from left to right
        f = 0
        for i in range(N):
            if dominoes[i] == 'R':
                f = N
            elif dominoes[i] == 'L':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] += f

        # Populate forces going from right to left
        f = 0
        for i in range(N-1, -1, -1):
            if dominoes[i] == 'L':
                f = N
            elif dominoes[i] == 'R':
                f = 0
            else:
                f = max(f-1, 0)
            force[i] -= f

        result = ''
        for f in force:
            if f == 0:
                result += '.'
            elif f > 0:
                result += 'R'
            else:
                result += 'L'
        return result


print(Solution().pushDominoes('..R...L..R.'))
# ..RR.LL..RR
