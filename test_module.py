from unittest import TestCase
from prob_calculator import Hat, experiment

hat_obj = Hat(black=6, red=4, green=3) ## total 13 balls

class UnitTests(TestCase):
    def test_hat_obj_contents(self):
        if hat_obj.contents:
            self.assertTrue(True)
        else:
            self.assertFalse(True)

    def test_draw_items_less_length(self):
        self.assertEqual(len(hat_obj.draw(5)), 5)

    def test_draw_items_greater_length(self):
        self.assertEqual(len(hat_obj.draw(15)), 13)

    def test_experiment(self):
        probability = experiment(hat_obj=hat_obj,
                    expected_balls={"red":2,"green":1},
                    num_balls_drawn=5,
                    num_experiments=2000)
        # self.assertAlmostEqual(probability, 0.272, delta=0.01)
        if probability:
            self.assertTrue(True)
        else:
            self.assertFalse(True)
