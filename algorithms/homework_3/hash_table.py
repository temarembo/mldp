class HashTable:
    def __init__(self, capacity=8):
        if capacity < 1:
            capacity = 1

        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _get_index(self, key):
        return hash(key) % self.capacity

    def _resize(self):
        old_buckets = self.buckets

        self.capacity *= 2
        self.buckets = [[] for _ in range(self.capacity)]
        self.size = 0

        for bucket in old_buckets:
            for item in bucket:
                self.put(item[0], item[1])

    def put(self, key, value):
        index = self._get_index(key)
        bucket = self.buckets[index]

        # Если ключ уже существует — обновляем значение
        for item in bucket:
            if item[0] == key:
                item[1] = value
                return

        # Если добавление нового элемента слишком сильно
        # заполнит таблицу — увеличиваем её
        if (self.size + 1) / self.capacity > 0.75:
            self._resize()
            index = self._get_index(key)
            bucket = self.buckets[index]

        bucket.append([key, value])
        self.size += 1

    def get(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]

        for item in bucket:
            if item[0] == key:
                return item[1]

        raise KeyError(key)

    def delete(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]

        for i in range(len(bucket)):
            if bucket[i][0] == key:
                value = bucket[i][1]
                bucket.pop(i)
                self.size -= 1
                return value

        raise KeyError(key)

    def contains(self, key):
        index = self._get_index(key)
        bucket = self.buckets[index]

        for item in bucket:
            if item[0] == key:
                return True

        return False

    def __len__(self):
        return self.size
