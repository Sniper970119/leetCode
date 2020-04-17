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


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.base = 0
        self.key_queue = []
        self.value_queue = []

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if self.base == 0:
            return -1
        if key not in self.key_queue:
            return -1
        key_idx = self.key_queue.index(key)
        value = self.value_queue[key_idx]
        self.key_queue.remove(key)
        self.key_queue.append(key)
        self.value_queue.remove(self.value_queue[key_idx])
        self.value_queue.append(value)
        return value
        pass

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.key_queue:
            key_idx = self.key_queue.index(key)
            self.value_queue[key_idx] = value
            self.get(key)
            return
        if self.base == self.capacity:
            self.key_queue.remove(self.key_queue[0])
            self.value_queue.remove(self.value_queue[0])
            self.base -= 1
        self.base += 1
        self.key_queue.append(key)
        self.value_queue.append(value)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

if __name__ == '__main__':
    capacity = 2
    obj = LRUCache(capacity)
    print(obj.get(2))
    obj.put(2, 6)
    print(obj.get(1))
    obj.put(1, 5)
    obj.put(1, 2)
    print(obj.get(1))
    print(obj.get(2))


