import os
from multiprocessing import Process


class YTMultiprocessing:
    def run_processing(self, target, iterable_data, dictionary_data):
        processes = []
        data = self.iterable_data_equal_parts(iterable_data)
        for core in range(os.cpu_count()):
            if not data:
                processes.append(Process(target=target))
            else:
                processes.append(Process(target=target, args=data[core], kwargs=dictionary_data))

        for process in processes:
            process.start()

        for process in processes:
            process.join()

    def iterable_data_equal_parts(self, iterable_data):
        equal_parts_by_num = os.cpu_count()
        item_num = len(iterable_data) / equal_parts_by_num
        if len(iterable_data) % equal_parts_by_num != 0:
            item_num += 1
        data = [iterable_data[i:i + int(item_num)] for i in range(0, len(iterable_data), int(item_num))]
        return tuple(data)
