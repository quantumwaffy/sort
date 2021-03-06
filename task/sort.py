from abc import ABC, abstractmethod
import datetime as dt

class SortData(ABC):

    @classmethod
    def timedec(self,func):
        def inner(*args, **kwargs):
            start = dt.datetime.now()
            rec = func(*args, **kwargs)
            delta = dt.datetime.now() - start
            print('Function finished in {} ms'.format(delta.microseconds))
            return rec
        return inner

    @abstractmethod
    def sort(self, list):
        pass

    def getdata(self, file):
        with open(file,"r") as f:
            for line in f.readlines():
                self.list = [int(item) for item in line.split(',')]
        return self.list

    def checkint(self, list):
        if all(isinstance(elem, int) for elem in list):
            return True
        else:
            print("List have not int elements")
            return False


class BubleSort(SortData):

    @SortData.timedec
    def sort(self, list):
        if super().checkint(list):
            for i in range(len(list) - 1):
                for j in range(len(list) - i - 1):
                    if list[j] > list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
        return list


class SelectionSort(SortData):

    @SortData.timedec
    def sort(self, list):
        if super().checkint(list):
                for i in range(len(list)):
                    lowest_index = i
                    for j in range(i + 1, len(list)):
                        if list[j] < list[lowest_index]:
                            lowest_index = j
                    list[i], list[lowest_index] = list[lowest_index], list[i]
        return list


class InsertionSort(SortData):

    @SortData.timedec
    def sort(self, list):
        if super().checkint(list):
            for i in range(1, len(list)):
                item_ins = list[i]
                j = i - 1
                while j >= 0 and list[j] > item_ins:
                    list[j + 1] = list[j]
                    j -= 1
                list[j + 1] = item_ins
        return list

class MergeSort(SortData):
    '''I spent a lot of time making a decorator for a recursive function.
    I failed.
    I will deal with this later'''
    def merge_sort(self,left_list, right_list):
        list = []
        left_list_index = right_list_index = 0
        left_list_length, right_list_length = len(left_list), len(right_list)
        for i in range(left_list_length + right_list_length):
            if left_list_index < left_list_length and right_list_index < right_list_length:
                if left_list[left_list_index] <= right_list[right_list_index]:
                    list.append(left_list[left_list_index])
                    left_list_index += 1
                else:
                    list.append(right_list[right_list_index])
                    right_list_index += 1
            elif left_list_index == left_list_length:
                list.append(right_list[right_list_index])
                right_list_index += 1
            elif right_list_index == right_list_length:
                list.append(left_list[left_list_index])
                left_list_index += 1
        self.end = dt.datetime.now()
        return list

    def sort(self, list):

        if super().checkint(list):
            self.start = dt.datetime.now()
            if len(list) <= 1:
                return list
            mid = len(list) // 2
            left_list = self.sort(list[:mid])
            right_list = self.sort(list[mid:])
        return self.merge_sort(left_list, right_list)

    def time_merge(self):
        delta = self.end - self.start
        print('Function finished in {} ms'.format(int(delta.microseconds)))
        return delta
