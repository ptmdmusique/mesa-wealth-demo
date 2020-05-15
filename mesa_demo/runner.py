import matplotlib.pyplot as plt
from MoneyModel import *

model = MoneyModel(10)
for i in range(10):
    model.step()

agent_wealth = [a.wealth for a in model.schedule.agents]
plt.hist(agent_wealth)
plt.show()