
# Tracking memory allocation in python

import tracemalloc

class MemoryAllocationTrace: 
    top_stats = None
    snapshot : tracemalloc.Snapshot
    snapshot1 : tracemalloc.Snapshot
    snapshot2 : tracemalloc.Snapshot

    def start_tracemalloc(self) -> None: 
        tracemalloc.start()

    def gatter_top_stats(self) -> None: 
        self.snapshot = tracemalloc.take_snapshot()
        self.top_stats = self.snapshot.statistics('lineno')

    def get_first_snapshot(self) -> None: 
        self.snapshot1 = tracemalloc.take_snapshot()

    def get_second_snapshot(self) -> None: 
        self.snapshot2 = tracemalloc.take_snapshot()

    def get_snapshot_differences(self) -> None: 
        self.top_stats = self.snapshot2.compare_to(self.snapshot1, 'lineno')

    def display_stats(self) -> None: 
        for stat in self.top_stats[:10]: 
            print(stat)



if __name__ == '__main__': 
    mat_instance = MemoryAllocationTrace()

    # Application invocation

    mat_instance.gatter_top_stats()
    mat_instance.display_stats()


    # Another approach to find the differences between snapshots 

    mat_instance.get_first_snapshot()

    # Call routine 

    mat_instance.get_second_snapshot()

    mat_instance.get_snapshot_differences()
    mat_instance.display_stats()


