import datetime
import hashlib

class Block:
    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash(data)
      self.next = None

    def calc_hash(self, data):
        hash_str = data.encode('utf-8')
        sha = hashlib.sha256()
        sha.update(hash_str)
        return sha.hexdigest()


class BlockChain:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, value):
        self.size += 1
        node = self.head

        if node is None:
            block = Block(datetime.datetime.now(), value, None)
            self.head = block
        else:
            while node.next:
                node = node.next
            node.next = Block(datetime.datetime.now(), value, node.hash)


chain = BlockChain()
chain.append('data for a')
chain.append('data for b')
chain.append('data for c')
