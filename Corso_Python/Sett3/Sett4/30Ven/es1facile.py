#2.5
#200 pezzi reali
pezzi = 200
difettosi = 15

#true positive & false positive (data)
tp = 12
fp = 6

#false negative
fn = difettosi - tp #3

#true negative
tn = pezzi -tp -fp -fn

#accuracy (how many true)
acc = (tp+tn)/pezzi

#precision (how many positive are true)
prec = tp / (tp+fp)

#recall (how many positives found)
recall = tp / (tp + fn)

#f1 score (mean of prec & recall, punishes far away values with multiplication)
f1score = 2*prec*recall / (prec+recall)

print("Totale: ", pezzi)

print("\nMANUALE")
print(f"TP: {tp} TN: {tn}  FP: {fp} FN: {fn}")

print("\nAccuracy score: ", acc)
print("Precision score: ", prec)
print("Recall score: ", recall)
print("F1 score: ", f1score)

#sklearn test
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

###
y_true = [0]*185 + [1]*15
y_pred = (
    [0]*179 +  # TN
    [1]*6   +  # FP
    [0]*3   +  # FN
    [1]*12     # TP
)
###

print("\nSKLEARN")

tn, fp, fn, tp = confusion_matrix(y_true, y_pred).ravel()
print(confusion_matrix(y_true, y_pred))
print(f"TP: {tp} TN: {tn}  FP: {fp} FN: {fn}")

acc = accuracy_score(y_true, y_pred)
prec = precision_score(y_true, y_pred)
recall = recall_score(y_true, y_pred)
f1score = f1_score(y_true, y_pred)

print("\nAccuracy score: ", acc)
print("Precision score: ", prec)
print("Recall score: ", recall)
print("F1 score: ", f1score)

#per un sistema antifrode dove non vogliamo falsi positivi,
# vorremmo utilizzare KNC con una soglia alta per casi positivi,
# perché la sua precisione e più alta.