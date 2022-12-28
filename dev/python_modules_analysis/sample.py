# numpy ok
import numpy as np
np.random.seed(42)
data = np.random.randint(0,10,size=(3,2))

# pandas ok
import pandas as pd
df = pd.DataFrame( data=data , columns=['x','y'])

# matplotlib backend? agg -> tkinter
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.scatter(*data)
#plt.show()
# <stdin>:1: UserWarning: Matplotlib is currently using agg, which is a non-GUI backend, so cannot show the figure.
plt.savefig('mpl_test')

# seaborn
import seaborn as sns
sns.set_theme(style="darkgrid")
# Load an example dataset with long-form data
fmri = sns.load_dataset("fmri")
# Plot the responses for different events and regions
sns.lineplot(x="timepoint", y="signal", hue="region", style="event", data=fmri)
# save as png
sns.mpl.pyplot.savefig('seaborn_test')

