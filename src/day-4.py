import argparse
import collections
import datetime
import enum
import re

class SleepEvent(enum.Enum):
        ASLEEP = 1
        WAKE_UP = 2

def main(args):
        data = []
        with open(args.path, 'r') as f:
                for line in f:
                        parts = line.strip().split()
                        timestamp = '{} {}'.format(parts[0][1:], parts[1][:-1])
                        if parts[3] == 'asleep':
                                event = SleepEvent.ASLEEP
                        elif parts[3] == 'up':
                                event = SleepEvent.WAKE_UP
                        else:
                                event = int(parts[3][1:])
                        data.append((timestamp, event))
        data.sort()

        current_guard = None
        total_time_asleep = collections.defaultdict(int)
        minutes_asleep = {}
        for i, entry in enumerate(data):
                timestamp, event = entry
                if type(event) is int:
                        current_guard = event
                elif event == SleepEvent.WAKE_UP:
                        assert(data[i - 1][1] == SleepEvent.ASLEEP)
                        previous_timestamp = data[i - 1][0]
                        previous_day, previous_hour_minute = previous_timestamp.split()
                        previous_hour, previous_minute = previous_hour_minute.split(':')
                        day, hour_minute = timestamp.split()
                        hour, minute = hour_minute.split(':')

                        assert(day == previous_day)
                        assert(hour == '00' and previous_hour == '00')
                        for m in range(int(previous_minute), int(minute)):
                                total_time_asleep[current_guard] += 1
                                if current_guard not in minutes_asleep:
                                        minutes_asleep[current_guard] = collections.defaultdict(int)
                                minutes_asleep[current_guard][m] += 1

        guard_id = sorted(total_time_asleep.items(), key=lambda x: x[1], reverse=True)[0][0]
        best_minute = sorted(minutes_asleep[guard_id].items(), key=lambda x: x[1], reverse=True)[0][0]
        print('Part one:', guard_id * best_minute)

        max_count = None
        max_g_id = None
        max_best_minute = None
        for g_id in total_time_asleep.keys():
                best_minute, count = sorted(minutes_asleep[g_id].items(), key=lambda x: x[1], reverse=True)[0]
                if max_count is None:
                        max_count = count
                        max_best_minute = best_minute
                        max_g_id = g_id
                elif count > max_count:
                        max_count = count
                        max_best_minute = best_minute
                        max_g_id = g_id
        print('Part two:', max_g_id * max_best_minute)

if __name__ == '__main__':
	parser = argparse.ArgumentParser()
	parser.add_argument('path')
	args = parser.parse_args()
	main(args)
