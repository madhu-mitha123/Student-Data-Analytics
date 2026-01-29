import pandas as pd
import matplotlib.pyplot as plt
import os

def main():
    # Load dataset
    file_path = 'student_performance.csv'
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.\n")
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return

    # Create plots directory
    os.makedirs('plots', exist_ok=True)

    # Exploratory Data Analysis (EDA)
    print("--- First 5 Rows ---")
    print(df.head(), "\n")

    print("--- DataFrame Info ---")
    print(df.info(), "\n")

    print("--- Summary Statistics ---")
    print(df.describe(), "\n")

    print("--- Missing Values ---")
    print(df.isnull().sum(), "\n")

    # Visualizations
    
    # 1. Histogram of Final Scores
    plt.figure(figsize=(8, 6))
    plt.hist(df['Final_Score'], bins=10, color='skyblue', edgecolor='black')
    plt.title('Distribution of Final Scores')
    plt.xlabel('Final Score')
    plt.ylabel('Frequency')
    plt.grid(axis='y', alpha=0.75)
    plt.savefig('plots/histogram_final_score.png')
    print("Saved plots/histogram_final_score.png")
    plt.close()

    # 2. Scatter Plot: Study Hours vs. Final Score
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Study_Hours'], df['Final_Score'], color='green', alpha=0.7)
    plt.title('Study Hours vs. Final Score')
    plt.xlabel('Study Hours')
    plt.ylabel('Final Score')
    plt.grid(True)
    plt.savefig('plots/scatter_study_vs_score.png')
    print("Saved plots/scatter_study_vs_score.png")
    plt.close()

    # 3. Scatter Plot: Attendance vs. Final Score
    plt.figure(figsize=(8, 6))
    plt.scatter(df['Attendance'], df['Final_Score'], color='orange', alpha=0.7)
    plt.title('Attendance vs. Final Score')
    plt.xlabel('Attendance (%)')
    plt.ylabel('Final Score')
    plt.grid(True)
    plt.savefig('plots/scatter_attendance_vs_score.png')
    print("Saved plots/scatter_attendance_vs_score.png")
    plt.close()

    # 4. Bar Chart: Average Final Score by Gender
    avg_score_by_gender = df.groupby('Gender')['Final_Score'].mean()
    plt.figure(figsize=(8, 6))
    avg_score_by_gender.plot(kind='bar', color=['pink', 'blue'])
    plt.title('Average Final Score by Gender')
    plt.xlabel('Gender')
    plt.ylabel('Average Final Score')
    plt.xticks(rotation=0)
    plt.savefig('plots/bar_gender_avg_score.png')
    print("Saved plots/bar_gender_avg_score.png")
    plt.close()

    print("Analysis and visualization completed.")

if __name__ == "__main__":
    main()
