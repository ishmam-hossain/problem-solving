class ProductOfNumbers:

    def __init__(self):
        self.arr = [1]

    def add(self, num: int) -> None:
        if num == 0:
            self.arr = [1]
        else:
            self.arr.append(self.arr[-1] * num)

    def getProduct(self, k: int) -> int:
        if k >= len(self.arr):
            return 0
        return self.arr[-1] // self.arr[-k - 1]

# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)