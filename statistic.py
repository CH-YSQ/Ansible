import matplotlib.pyplot as plt
import numpy as np

# Number of instances
x = ["1", "2", "4", "8"]
# Average Req/Sec of three runs for each number of workers
y = [814.59, 647.51, 544.88, 545.97]

plt.title("Performance of service per number of instances")
plt.xlabel("Number of Instances")
plt.ylabel("Average Req/Sec")
plt.bar(x, y)
plt.show()
