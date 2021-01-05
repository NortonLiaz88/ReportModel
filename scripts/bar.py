import matplotlib.pyplot as plt
import seaborn as sns

titanic_dataset = sns.load_dataset("titanic")
clrs = ["#42b7bd", "#a834a8"]
sns.barplot(x = "class", y = "survived", hue = "embark_town", palette =clrs,ci = None, data = titanic_dataset)
plt.show()