# This entrypoint file to be used in development. Start by reading README.md
import prob_calculator
from unittest import main

prob_calculator.random.seed(95)
prob_calculator.random.seed(55)
hat = prob_calculator.Hat(blue=4, red=2, green=6)
print("hatdraw: ",hat.draw(2))

probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"blue": 2,
                    "red": 1},
    num_balls_drawn=4,
    num_experiments=3000)
print("Probability:", probability)
hat1 = prob_calculator.Hat(blue=3,red=2,green=6)
probability1 = prob_calculator.experiment(hat=hat1, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print("Probability1:", probability1)
hat2 = prob_calculator.Hat(red=5,blue=2)

print("Probability2:","actual draw: ", hat2.draw(2))
print("Probability2:","actual len: ", len(hat2.contents))

# Run unit tests automatically
main(module='test_module', exit=False)
