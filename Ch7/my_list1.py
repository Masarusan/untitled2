class NumList(list):
    #正の値を合計する
    def sum_plus_value(self):
        sum = 0
        for n in self:
            if n > 0:
                sum+= n
        return sum
    #負の値を０にする

    def remove_minus_value(self):
        for i in range(len(self)):
            if self[i] < 0:
                self[i] = 0

if __name__ == "__main__":
    lst = NumList([1,2,3,-4,9,-9])
    lst[1] = 4
    print("合計:{}".format(lst.sum_plus_value()))
    lst.remove_minus_value()
    print(lst)