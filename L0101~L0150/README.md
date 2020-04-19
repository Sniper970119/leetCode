# Sniper
[L0101](https://leetcode-cn.com/problems/symmetric-tree/): 递归分别判断

[L0102](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/): 用栈实现层序遍历

[L0103](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/): 还是树的遍历，只不过要加一个层级标签用来判断向哪个方向添加结点

[L0104](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/): 深度优先遍历记录树的高度

[L0105](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/):
[笔记链接](http://www.sniper97.cn/index.php/note/algorithm/2935/)

[L0106](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/): 根据后序遍历切割中序遍历递归

[L0107](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii/): L0102倒序输出

[L0108](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/): 二分法构造树

[L0109](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/): 链表转数组，二分法构造树

[L0110](https://leetcode-cn.com/problems/balanced-binary-tree/): 深搜+断言提前退出

[L0111](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/): 深搜

[L0112](https://leetcode-cn.com/problems/path-sum/): 也是遍历，多个判断而已。

[L0113](https://leetcode-cn.com/problems/path-sum/): 和上道题一样，多一个列表存储结果。

[L0114](https://leetcode-cn.com/problems/flatten-binary-tree-to-linked-list/): 前序遍历+链表生成

[L0115](https://leetcode-cn.com/problems/distinct-subsequences/): 这道题刚开始我用回溯做的，超时，然后就用递归，递归式为if si==tj,dpij=dpi-1 j-1 else dp ij = dp i j-1

[L0116](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node/): 层序遍历连指针

[L0117](https://leetcode-cn.com/problems/populating-next-right-pointers-in-each-node-ii/): 层序遍历连指针

[L0118](https://leetcode-cn.com/problems/pascals-triangle/): 杨辉三角

[L0119](https://leetcode-cn.com/problems/pascals-triangle-ii/): 杨辉三角

[L0120](https://leetcode-cn.com/problems/pascals-triangle-ii/): 动态规划

[L0121](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/): 遍历寻找最小值和最大值（要遍历不要用自带函数，因为遍历可以避免最大值出现在最小值之前的情况）

[L0122](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/): 贪心，以一天为单位，涨就买，跌就观望

[L0123](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/): 动态规划（有点难呜呜呜呜）[笔记](http://www.sniper97.cn/index.php/note/algorithm/3419/)

[L0124](https://leetcode-cn.com/problems/binary-tree-maximum-path-sum/): 深度优先遍历，每一个子树的最大结果向上传播到根节点。

[L0125](https://leetcode-cn.com/problems/valid-palindrome/): 处理非数字和字母的字符然后[::-1]比较

[L0126](https://leetcode-cn.com/problems/word-ladder-ii/): 深搜回溯，可以参考L0127的笔记，不过L0127是广搜，总体思想类似。

[L0127](https://leetcode-cn.com/problems/word-ladder/): [笔记](http://www.sniper97.cn/index.php/note/algorithm/3430/)

[L0128](https://leetcode-cn.com/problems/longest-consecutive-sequence/): 使用set，因为set使用树结构，因此插入lgn，查找也是lgn ，均小于n

[L0129](https://leetcode-cn.com/problems/sum-root-to-leaf-numbers/): 深搜

[L0130](https://leetcode-cn.com/problems/surrounded-regions/): 从边缘向内深搜

[L0131](https://leetcode-cn.com/problems/palindrome-partitioning/): 迭代递增结果集中的回文字串

[L0132](https://leetcode-cn.com/problems/palindrome-partitioning-ii/): 动态规划

[L0133](https://leetcode-cn.com/problems/palindrome-partitioning-ii/): 直接copy.deepcopy   python真香

[L0134](https://leetcode-cn.com/problems/gas-station/): 遍历判断

[L0135](https://leetcode-cn.com/problems/candy/): 从两侧进行两边循环，分别寻找满足条件的情况，最后将两次遍历的结果取最大值求和返回。

[L0136](https://leetcode-cn.com/problems/single-number/): 去重乘2，减去原列表就是只出现一次的数字

[L0137](https://leetcode-cn.com/problems/single-number-ii/): 去重乘3，减去原列表除二，就是只出现一次的数字

[L0138](https://leetcode-cn.com/problems/copy-list-with-random-pointer/): deepcopy

[L0139](https://leetcode-cn.com/problems/word-break/): dp

[L0140](https://leetcode-cn.com/problems/word-break-ii/): dfs

[L0141](https://leetcode-cn.com/problems/linked-list-cycle/): 遍历链表更改数据，如遇到更改过的点则True

[L0142](https://leetcode-cn.com/problems/linked-list-cycle-ii/): 将遍历过的点送入set，重复返回

[L0143](https://leetcode-cn.com/problems/reorder-list/): 链表操作

[L0144](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/): 前序遍历

[L0145](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/): 后序遍历

[L0146](https://leetcode-cn.com/problems/lru-cache/): 模仿队列进行更新即可

[L0147](https://leetcode-cn.com/problems/insertion-sort-list/): 插入排序，只不过列表换成数组

[L0148](https://leetcode-cn.com/problems/sort-list/): 链表的归并排序

[L0149](https://leetcode-cn.com/problems/max-points-on-a-line/): 穷举所有点对的斜率，然后添加到字典，判断有多少对点斜率相同。

[L0149](https://leetcode-cn.com/problems/evaluate-reverse-polish-notation/): 栈操作





