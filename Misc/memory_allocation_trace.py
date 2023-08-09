"""Module for tracking memory allocation in python"""

import tracemalloc

class MemoryAllocationTrace:
    """Memory allocation trace class """
    top_stats: list[tracemalloc.Statistic]
    top_stats_difference : list[tracemalloc.StatisticDiff]
    snapshot : tracemalloc.Snapshot
    snapshot1 : tracemalloc.Snapshot
    snapshot2 : tracemalloc.Snapshot

    def start_tracemalloc(self) -> None:
        """ Start tracemalloc method """
        try:
            tracemalloc.start()
        except MemoryError as memory_error:
            print(memory_error)
        except Exception as start_tracemalloc_ex:
            print(start_tracemalloc_ex)

    def get_top_stats(self) -> None:
        """ Get top stats method """
        try:
            self.snapshot = tracemalloc.take_snapshot()
            self.top_stats = self.snapshot.statistics('lineno')
        except RuntimeError as get_top_stats_ex:
            print(get_top_stats_ex)

    def get_first_snapshot(self) -> None:
        """Get first snapshot method """
        try:
            self.snapshot1 = tracemalloc.take_snapshot()
        except RuntimeError as get_first_snapshot_ex:
            print(get_first_snapshot_ex)

    def get_second_snapshot(self) -> None:
        """Get second snapshot method """
        try:
            self.snapshot2 = tracemalloc.take_snapshot()
        except RuntimeError as get_second_snapshot_ex:
            print(get_second_snapshot_ex)

    def get_snapshot_differences(self) -> None:
        """Get snapshot differences method """
        try:
            self.top_stats_difference = self.snapshot2.compare_to(self.snapshot1, 'lineno')
        except Exception as get_snapshot_diff_ex:
            print(get_snapshot_diff_ex)

    def display_stats(self) -> None:
        """ Display stats method """
        try:
            for stat in self.top_stats[:10]:
                print(stat)
        except Exception as display_stats_ex:
            print(display_stats_ex)

    def display_stats_difference(self) -> None:
        """Display stats differences method """
        try:
            for stat_diff in self.top_stats_difference[:10]:
                print(stat_diff)
        except Exception as ex:
            print(ex)

if __name__ == '__main__':
    mat_instance = MemoryAllocationTrace()

    # Application invocation
    mat_instance.get_top_stats()
    mat_instance.display_stats()

    # Another approach to find the differences between snapshots
    mat_instance.get_first_snapshot()

    # Call routine
    mat_instance.get_second_snapshot()
    mat_instance.display_stats()

    # Snapshot differences
    mat_instance.get_snapshot_differences()
    mat_instance.display_stats_difference()
