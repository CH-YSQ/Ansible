import matplotlib.pyplot as plt
import numpy as np

# Number of instances
x = ["1", "2", "4", "8"]
# Average Req/Sec of three runs for each number of workers
y = [814.59, 647.51, 544.88, 545.97]

plt.ylabel("Average Request per Seconds")
plt.xlabel("Number of Instances")
plt.title("Performance in Request/Seconds per number of instances")
plt.bar(x, y)
plt.show()
