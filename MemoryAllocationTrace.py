
# Tracking memory allocation in python

import tracemalloc

class MemoryAllocationTrace: 
    top_stats = None
    snapshot1 = None
    snapshot2 = None

    def start_tracemalloc(self): 
        tracemalloc.start()

    def gatter_top_stats(self): 
        snapshot = tracemalloc.take_snapshot()
        self.top_stats = self.snapshot.statistics('lineno')

    def get_first_snapshot(self): 
        self.snapshot1 = tracemalloc.take_snapshot()

    def get_second_snapshot(self): 
        self.snapshot2 = tracemalloc.take_snapshot()

    def get_snapshot_differences(self): 
        self.top_stats = self.snapshot2.compare_to(self.snapshot1, 'lineno')

    def display_stats(self): 
        for stat in self.top_stats[:10]: 
            print(stat)


matInstance = MemoryAllocationTrace()

# Application invocation

matInstance.gatter_top_stats()
matInstance.display_stats()


# Another approach to find the differences between snapshots 

matInstance.get_first_snapshot()

# Call routine 

matInstance.get_second_snapshot()

matInstance.get_snapshot_differences()
matInstance.display_stats()


