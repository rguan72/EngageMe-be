class Video(object):
    def __init__(self, name, average_intervals):
        self.name = name
        self.average_intervals = average_intervals

    @staticmethod
    def from_dict(source):
        average_intervals = []
        for interval in source["average_intervals"]:
            average_intervals.append(interval.split(","))
        return {
            "name": source["name"],
            "average_intervals": average_intervals
        }

    def to_dict(self):
        return {
            "name": self.name,
            "average_intervals": self.average_intervals
        }

    def __repr__(self):
        return f"Name: {self.name}\nAverage Intervals: {self.average_intervals}"