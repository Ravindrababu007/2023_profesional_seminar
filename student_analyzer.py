import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

class StudentPerformanceAnalysisSystem:
    def __init__(self, master):
        # ...

    def analyze_performance(self):
        # Load the student performance dataset (assuming it's in a CSV file)
        dataset = pd.read_csv('student_performance.csv')

        # Split the dataset into features (X) and target (y)
        X = dataset.drop('grade', axis=1)  # Features: all columns except the 'grade'
        y = dataset['grade']  # Target: the 'grade' column

        # Split the data into training and testing sets
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        # Train a linear regression model
        model = LinearRegression()
        model.fit(X_train, y_train)

        # Make predictions on the test set
        y_pred = model.predict(X_test)

        # Provide recommendations based on the predictions
        recommendations = []
        for i, pred in enumerate(y_pred):
            if pred >= 90:
                recommendations.append(f"Student {i+1}: Excellent performance!")
            elif pred >= 80:
                recommendations.append(f"Student {i+1}: Good performance.")
            else:
                recommendations.append(f"Student {i+1}: Needs improvement.")

        # Display the analysis and recommendations
        messagebox.showinfo("Performance Analysis", "\n".join(recommendations))
