
# Tracking memory allocation in python

import tracemalloc

class MemoryAllocationTrace: 
    top_stats: list[tracemalloc.Statistic]
    top_stats_difference : list[tracemalloc.StatisticDiff]
    snapshot : tracemalloc.Snapshot
    snapshot1 : tracemalloc.Snapshot
    snapshot2 : tracemalloc.Snapshot

    def start_tracemalloc(self) -> None: 
        try:
            tracemalloc.start()
        except Exception as ex: 
            print(ex)

    def gatter_top_stats(self) -> None: 
        try: 
            self.snapshot = tracemalloc.take_snapshot()
            self.top_stats = self.snapshot.statistics('lineno')
        except Exception as ex: 
            print(ex)

    def get_first_snapshot(self) -> None: 
        try: 
            self.snapshot1 = tracemalloc.take_snapshot()
        except Exception as ex: 
            print(ex)

    def get_second_snapshot(self) -> None: 
        try: 
            self.snapshot2 = tracemalloc.take_snapshot()
        except Exception as ex: 
            print(ex)

    def get_snapshot_differences(self) -> None: 
        try: 
            self.top_stats_difference = self.snapshot2.compare_to(self.snapshot1, 'lineno')
        except Exception as ex: 
            print(ex)

    def display_stats(self) -> None: 
        try: 
            for stat in self.top_stats[:10]: 
                print(stat)
        except Exception as ex: 
            print(ex)

    def display_stats_difference(self) -> None: 
        try: 
            for stat_diff in self.top_stats_difference[:10]: 
                print(stat_diff)
        except Exception as ex: 
            print(ex)

if __name__ == '__main__': 
    mat_instance = MemoryAllocationTrace()

    # Application invocation

    mat_instance.gatter_top_stats()
    mat_instance.display_stats()


    # Another approach to find the differences between snapshots 

    mat_instance.get_first_snapshot()

    # Call routine 

    mat_instance.get_second_snapshot()
    mat_instance.display_stats()

    # Snapshot differences
    mat_instance.get_snapshot_differences()
    mat_instance.display_stats_difference()


