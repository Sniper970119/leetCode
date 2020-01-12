# -*- coding:utf-8 -*-

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows == len(s) or len(s) < numRows:
            return s
        s_len = len(s)
        pre_jump_len = 2 * numRows
        next_jump_len = -2
        current_idx = 0
        latest_idx = 0
        result = ''
        for i in range(numRows):
            if pre_jump_len > 2:
                pre_jump_len -= 2
            else:
                pre_jump_len = 2 * numRows - 2
            if next_jump_len < 2 * numRows-2:
                next_jump_len += 2
            else:
                next_jump_len = 0
            result = result + s[current_idx]
            latest_idx = current_idx
            for j in range(s_len):
                if current_idx + pre_jump_len < s_len:
                    result = result + s[current_idx + pre_jump_len]
                    current_idx = current_idx + pre_jump_len
                else:
                    current_idx = latest_idx + 1
                    break
                if next_jump_len == 0:
                    continue
                if current_idx + next_jump_len < s_len:
                    result = result + s[current_idx + next_jump_len]
                    current_idx = current_idx + next_jump_len
                else:
                    current_idx = latest_idx + 1
                    break
        return result
        pass


if __name__ == '__main__':
    s = 'PAYPALISHIRING'
    print(Solution().convert(s, 5))

# LEETCODEISHIRING
# LCIRETOESIIGEDHN 3
# LCIRETOESIIGEDHN
# LDREOEIIECIHNTSG 4
# LDREOEIIECIHNTSG

# PAYPALISHIRING
# PHASIYIRPLSIIGAN
# PHASIYIRPLIGAN
# PHASIYIRPLIGAN