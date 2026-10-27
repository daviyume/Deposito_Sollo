'''import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import metrics


cm = metrics.confusion_matrix(y_test, y_pred)

plt.figure(figsize=(6,4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues',
xticklabels=data.target_names,
yticklabels=data.target_names)
#1 choose what to display in heatmap
#2 choose if display text in the cells
#3 fmt means format. d is decimal integer
#cmap is style color of heatmap
#assign the class names to the tick labels

plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')

plt.show()'''