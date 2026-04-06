import heapq


class TriageSystem:
    arrival_counter = 0

    def __init__(self):
        self._queue = []

    @staticmethod
    def NextArrivalOrder():
        order = TriageSystem.arrival_counter
        TriageSystem.arrival_counter += 1
        return order

    def AddPatient(self, name, severity):
        if not name or not isinstance(name, str):
            raise ValueError("Invalid name")

        if not isinstance(severity, int) or severity < 1 or severity > 5:
            raise ValueError("Invalid severity")

        arrival = TriageSystem.NextArrivalOrder()

        heapq.heappush(self._queue, (-severity, arrival, name))

    def ProcessNext(self):
        if self.IsEmpty():
            return None

        severity, arrival, name = heapq.heappop(self._queue)
        return (name, -severity)

    def PeekNext(self):
        if self.IsEmpty():
            return None

        severity, arrival, name = self._queue[0]
        return (name, -severity)

    def IsEmpty(self):
        return len(self._queue) == 0

    def Size(self):
        return len(self._queue)

    def Clear(self):
        self._queue.clear()