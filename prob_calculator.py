import copy
import random

class Hat:
    def __init__(self, **kwargs): ## here args are the colored balls
        # print(kwargs)
        self.contents = []
        for key, value in kwargs.items():
            self.contents.extend([key] * value)
        # print(self.contents)

    def draw(self, number_of_balls):
        if number_of_balls > len(self.contents):
            return self.contents
        removed_balls = []
        for i in range(number_of_balls):
            a_random_element = random.choice(self.contents)
            removed_balls.append(a_random_element)
            self.contents.remove(a_random_element)
        return removed_balls

def experiment(
        hat_obj: Hat, 
        expected_balls: dict, 
        num_balls_drawn: int, 
        num_experiments: int
) -> float:
    
    success = 0
    
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat_obj)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # print(drawn_balls)
        # print(expected_balls)
        # print(hat_copy.contents)
        # print('----------------')

        flag = True
        for key, value in expected_balls.items():
            if drawn_balls.count(key) < value:
                flag = False
                break
        if flag:
            success += 1
    return success/num_experiments

if __name__ == '__main__':
    # obj = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    hat_obj = Hat(black=6, red=4, green=3)
    probability = experiment(hat_obj=hat_obj,
                    expected_balls={"red":2,"green":1},
                    num_balls_drawn=5,
                    num_experiments=2000)
    print(probability)
