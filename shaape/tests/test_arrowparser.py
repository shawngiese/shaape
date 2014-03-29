from shaape.arrowparser import ArrowParser
from shaape.rightarrow import RightArrow
from shaape.leftarrow import LeftArrow
from shaape.uparrow import UpArrow
from shaape.downarrow import DownArrow
import nose
import unittest
from nose.tools import *

class TestArrowParser(unittest.TestCase):
    def test_init(self):
        arrowparser = ArrowParser()
        assert arrowparser.parsed_data() == []
        assert arrowparser.drawable_objects() == []

    def test_run(self):
        arrowparser = ArrowParser()
        data = ['< > ^ v']
        objects = []
        arrowparser.run(data, objects)
        assert arrowparser.parsed_data() == data
        assert arrowparser.drawable_objects() == objects, str(arrowparser.drawable_objects()) + str(objects)
        assert len(objects) == 4
        assert [o for o in objects if type(o) == RightArrow]
        assert [o for o in objects if type(o) == LeftArrow]
        assert [o for o in objects if type(o) == UpArrow]
        assert [o for o in objects if type(o) == DownArrow]
        
