import matplotlib.pyplot as plt
import numpy as np

# Number of instances
x = ["1", "2", "4", "8"]

# Average Req/Sec of three runs for each number of workers
y = [815.59, 648.51, 543.88, 548.97]

plt.title("Performance of service per number of instances")
plt.xlabel("Number of Instances")
plt.ylabel("Average Req/Sec")
plt.bar(x, y)
plt.show()
