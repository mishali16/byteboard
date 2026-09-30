import unittest
from pathlib import Path

from byteboard.inspect import inspect_function
from byteboard.loader import load_function


class InspectTest(unittest.TestCase):
    def test_reports_bytecode(self):
        func = load_function(Path(__file__).parents[1] / "samples" / "snippet.py", "score_move")
        data = inspect_function(func)
        opnames = {item["opname"] for item in data["instructions"]}
        self.assertIn("RETURN_VALUE", opnames)
        self.assertTrue(data["edges"])


if __name__ == "__main__":
    unittest.main()
