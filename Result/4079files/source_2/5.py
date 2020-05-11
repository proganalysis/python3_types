import unittest
from event import EventHook


class CompositeProgress:
    def __init__(self, spans, target):
        self.spans = spans
        self.target = target
        for s in self.spans:
            s.on_change += lambda span: self.update()

    def update(self):
        """ compute a new total for this composite progress """
        total = 0
        current = 0
        for s in self.spans:
            total += s.max-s.min
            current += s.current-s.min
        self.set(current, total)

    def set(self, current, total):
        self.target.max = total
        self.target.update(current)


class CompositeProgressTest(unittest.TestCase):

    def test_composite_progress(self):
        # span1 is 1/4 of the progress, span 2 is 3/4. Total is 400
        spans = [ ProgressSpan(100,200), ProgressSpan(1000,1300)]
        target = ProgressSpan(0,0)
        c = CompositeProgress(spans, target)
        spans[0].update(150)        # 1/2 span 1 complete, overall 1/8
        self.assertEqual(target.current, 50)
        self.assertEqual(target.max, 400)
        spans[1].update(1300)       # span 2 complete, total is now 3/4+1/8 = 350
        self.assertEqual(target.current, 350)
        self.assertEqual(target.max, 400)
        spans[0].update(200)
        self.assertEqual(target.current, 400)
        self.assertEqual(target.max, 400)


class ProgressSpan:
    def __init__(self,max=0,min=0,name=""):
        self.max = max
        self.min = min
        self.name = name
        self.current = min
        self.on_change = EventHook()

    def update(self, current):
        if current!=self.current:
            self.current = current
            self.on_change.fire(self)

    def __iadd__(self, other):
        self.update(self.current + other)
        return self

class ProgressSpanTest(unittest.TestCase):
    updated = None

    def update(self, progress):
        self.updated = progress

    def check_updated(self, span):
        self.assertEqual(self.updated, span)
        self.updated = None

    def test_progress_update(self):
        span = ProgressSpan(100, 50, "on the case")
        self.assertEqual(span.min, 50)
        self.assertEqual(span.max, 100)
        self.assertEqual(span.name, "on the case")
        self.assertEqual(span.current, 50)
        span.on_change += lambda span: self.update(span)
        span.update(75)
        self.check_updated(span)
        self.assertEqual(span.current, 75)
        span.update(75)         # same value, no update
        self.assertEqual(self.updated, None)
        self.assertEqual(span.current, 75)

        span += 25
        self.check_updated(span)
        self.assertEqual(span.current, 100)

