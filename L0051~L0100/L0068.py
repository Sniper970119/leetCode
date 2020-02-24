# -*- coding:utf-8 -*-

"""
      ┏┛ ┻━━━━━┛ ┻┓
      ┃　　　　　　 ┃
      ┃　　　━　　　┃
      ┃　┳┛　  ┗┳　┃
      ┃　　　　　　 ┃
      ┃　　　┻　　　┃
      ┃　　　　　　 ┃
      ┗━┓　　　┏━━━┛
        ┃　　　┃   神兽保佑
        ┃　　　┃   代码无BUG！
        ┃　　　┗━━━━━━━━━┓
        ┃　　　　　　　    ┣┓
        ┃　　　　         ┏┛
        ┗━┓ ┓ ┏━━━┳ ┓ ┏━┛
          ┃ ┫ ┫   ┃ ┫ ┫
          ┗━┻━┛   ┗━┻━┛
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        def find_one_line(word_idx):
            """
            寻找可以放在一行中的单词
            :param word_idx:
            :return:
            """
            current_length = len(words[word_idx])
            temp_str = words[word_idx]
            # temp_list = [words[word_idx]]
            word_idx += 1
            if word_idx >= len(words):
                res_list.append(temp_str)
                return
            # 挑选单词
            while current_length + len(words[word_idx]) + 1 <= maxWidth:
                temp_str = temp_str + ' ' + words[word_idx]
                # temp_list.append(' ' + words[word_idx])
                word_idx += 1
                if word_idx >= len(words):
                    break
                # current_length += len(words[word_idx])+1
                current_length = len(temp_str)
            res_list.append(temp_str)
            if word_idx < len(words):
                find_one_line(word_idx)

        def check_space():
            """
            检查处理空格
            :return:
            """
            # 处理前n行
            for i in range(len(res_list) - 1):
                current_length = len(res_list[i])
                space_length = maxWidth - current_length
                temp_cache = res_list[i].split(' ')
                if len(temp_cache) - 1 > 0:
                    m, n = divmod(space_length, len(temp_cache) - 1)
                    for j in range(n):
                        temp_cache[j] = temp_cache[j] + ' ' * (m + 1 + 1)
                    for j in range(n, len(temp_cache) - 1):
                        temp_cache[j] = temp_cache[j] + ' ' * (m + 1)
                else:
                    if space_length != 0:
                        m = 0
                        n = space_length - 1
                        temp_cache[0] = temp_cache[0] + ' ' * (m + n + 1)
                    else:
                            pass

                res_str = ''
                for j in range(len(temp_cache)):
                    res_str = res_str + temp_cache[j]
                res.append(res_str)
            # 处理最后一行
            current_length = len(res_list[-1])
            space_length = maxWidth - current_length
            temp_cache = res_list[-1].split(' ')
            for i in range(len(temp_cache) - 1):
                temp_cache[i] = temp_cache[i] + ' '
            temp_cache[-1] = temp_cache[-1] + ' ' * space_length
            res_str = ''
            for j in range(len(temp_cache)):
                res_str = res_str + temp_cache[j]
            res.append(res_str)

        res_list = []
        res = []
        find_one_line(0)
        check_space()
        return res


if __name__ == '__main__':
    words = ["What", "must", "be", "acknowledgment", "shall", "be"]
    words = ["Science", "is", "what", "we", "understand", "well", "enough", "to", "explain", "to", "a", "computer.",
             "Art", "is", "everything", "else", "we", "do"]
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words = ["Listen", "to", "many,", "speak", "to", "a", "few."]
    maxWidth = 6
    print(Solution().fullJustify(words, maxWidth))
