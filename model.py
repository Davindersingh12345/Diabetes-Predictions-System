import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\important\sem 5\INT 234\BRFSS_2021_Categorical.csv")
df
df.isnull().sum()
df = df.dropna()

df.isnull().sum()

#EDA
import matplotlib.pyplot as plt
import seaborn as sns

# Histogram for Age
plt.figure(figsize=(6,4))
sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Distribution of Age")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()

# Histogram for BMI
plt.figure(figsize=(6,4))
sns.histplot(df['BMI'], bins=30, kde=True)
plt.title("Distribution of BMI")
plt.xlabel("BMI")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(5,4))
df['Smoked'].value_counts().plot(kind='bar')
plt.title("Smoking Status Distribution")
plt.xlabel("Smoking Status")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()



plt.figure(figsize=(5,4))
df['Physical Activity'].value_counts().plot(kind='bar')
plt.title("Physical Activity Distribution")
plt.xlabel("Physically Active")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()


import matplotlib.pyplot as plt

plt.figure(figsize=(7,4))
df['General Health'].value_counts().plot(kind='bar')
plt.title("General Health Distribution")
plt.xlabel("General Health Status")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()



df = pd.get_dummies(df, columns=['Physical Activity', 'Smoked' , 'General Health' , 'Gender', 'Diabetic','High_BP'], drop_first=True,dtype=int)

print(df.columns.tolist())

X = df.drop('Diabetic_Yes', axis=1)
y = df['Diabetic_Yes']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
X_train, X_test, y_train, y_test

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Logistic Regression
from sklearn.linear_model import LogisticRegression
lr_model = LogisticRegression(max_iter=1000)
lr_model.fit(X_train_scaled,y_train)
lr_pred = lr_model.predict(X_test_scaled)
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
lr_accuracy =  accuracy_score(y_test, lr_pred)
print("Accuracy:",lr_accuracy)
# Confusion Matrix
lr_cm = confusion_matrix(y_test, lr_pred)
print("Confusion Matrix:\n", lr_cm)
# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, lr_pred))

# DecisionTreeClassifier
from sklearn.tree import DecisionTreeClassifier, plot_tree
Dtc_model = DecisionTreeClassifier(max_depth = 2, random_state=42)
Dtc_model.fit(X_train, y_train)
Dtc_pred = Dtc_model.predict(X_test)
DTC_accuracy = accuracy_score(y_test, Dtc_pred)
print("Accuracy:", DTC_accuracy)
# Confusion Matrix
Dtc_cm = confusion_matrix(y_test, Dtc_pred)
print("Confusion Matrix:\n", Dtc_cm)
# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, Dtc_pred))
plt.figure(figsize=(20,10))
sns.heatmap(confusion_matrix(y_test, Dtc_pred), annot = True, cmap = 'Purples', fmt = 'g')
plt.title('Confusion Matrix - Decision Tree')
plot_tree(Dtc_model, filled=True, feature_names=X_train.columns.astype(str), class_names=["Non-Diabetic", "Diabetic"], rounded=True, fontsize=8)
plt.show()

# RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
Rfc_model = RandomForestClassifier(n_estimators=100, random_state=42)
Rfc_model.fit(X_train, y_train)
Rfc_pred = Rfc_model.predict(X_test)
Rfc_accuracy = accuracy_score(y_test, Rfc_pred)
print("Accuracy:", Rfc_accuracy)
# Confusion Matrix
Rfc_cm = confusion_matrix(y_test, Rfc_pred)
print("Confusion Matrix:\n", Rfc_cm)
# Classification Report
print("\nClassification Report:\n")
print(classification_report(y_test, Rfc_pred))

#MLP Classifier
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

ann_model = MLPClassifier(
    hidden_layer_sizes=(64, 32),
    activation='relu',
    solver='adam',
    max_iter=1000,
    random_state=42
)

ann_model.fit(X_train_scaled, y_train) 

ann_pred = ann_model.predict(X_test_scaled)

ann_accuracy = accuracy_score(y_test, ann_pred)

print("----- Neural Network (ANN) Results -----")
print("Accuracy:", ann_accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, ann_pred))

print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, ann_pred))



# Models Comparison
# Dictionary of model accuracies
accuracies = {
    "Logistic Regression": lr_accuracy,
    "Decision Tree": DTC_accuracy,
    "Random Forest": Rfc_accuracy,
    "MLP Classifier": ann_accuracy
}

# Print all accuracies
print("\n----- Model Accuracies -----")
for model, acc in accuracies.items():
    print(f"{model}: {acc:.4f}")

# Find best model
best_model = max(accuracies, key=accuracies.get)
best_accuracy = accuracies[best_model]

print("\n===== BEST MODEL =====")
print(f"Best Model: {best_model}")
print(f"Accuracy: {best_accuracy:.4f}")

from sklearn.metrics import precision_score, recall_score, f1_score

# Store predictions in a dictionary
predictions = {
    "Logistic Regression": lr_pred,
    "Decision Tree": Dtc_pred,
    "Random Forest": Rfc_pred,
    "MLP Classifier": ann_pred
}

print("\n===== Precision, Recall & F1 Score for Each Model =====")

for model_name, pred in predictions.items():
    precision = precision_score(y_test, pred)
    recall = recall_score(y_test, pred)
    f1 = f1_score(y_test, pred)

    print(f"\n--- {model_name} ---")
    print(f"Precision: {precision:.4f}")
    print(f"Recall:    {recall:.4f}")
    print(f"F1 Score:  {f1:.4f}")

accuracies = {"Logistic Regression": lr_accuracy,
    "Decision Tree": DTC_accuracy,
    "Random Forest": Rfc_accuracy,
    "MLP Classifier": ann_accuracy
                   }
colors =  ['skyblue', 'lightgreen', 'lightcoral', 'plum']


plt.figure(figsize=(10,7))
bars = plt.bar(accuracies.keys(), accuracies.values(), color=colors)
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy")
plt.ylim(0, 1)



# Add value labels on top of bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, height + 0.01, f"{height:.3f}", ha='center', va='bottom')

plt.show()

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

# Logistic Regression
sns.heatmap(confusion_matrix(y_test, lr_pred), annot=True, fmt='d',
            cmap='Blues', ax=axes[0, 0])
axes[0, 0].set_title("Logistic Regression")
axes[0, 0].set_xlabel("Predicted")
axes[0, 0].set_ylabel("Actual")

# Decision Tree
sns.heatmap(confusion_matrix(y_test, Dtc_pred), annot=True, fmt='d',
            cmap='Greens', ax=axes[0, 1])
axes[0, 1].set_title("Decision Tree")
axes[0, 1].set_xlabel("Predicted")
axes[0, 1].set_ylabel("Actual")

# Random forest Classifier"
sns.heatmap(confusion_matrix(y_test, Rfc_pred), annot=True, fmt='d',
            cmap='Oranges', ax=axes[1, 0])
axes[1, 0].set_title("Random forest Classifier")
axes[1, 0].set_xlabel("Predicted")
axes[1, 0].set_ylabel("Actual")

# MLP
sns.heatmap(confusion_matrix(y_test, ann_pred), annot=True, fmt='d',
            cmap='Purples', ax=axes[1, 1])
axes[1, 1].set_title("MLP")
axes[1, 1].set_xlabel("Predicted")
axes[1, 1].set_ylabel("Actual")

plt.tight_layout()
plt.show()