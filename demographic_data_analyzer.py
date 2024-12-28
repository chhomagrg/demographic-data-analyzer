import pandas as pd

def calculate_demographic_data(print_data=True):
    # Read the dataset
    df = pd.read_csv('adult.data.csv')

    # Ensure columns are correctly interpreted
    numeric_columns = ['age', 'education-num', 'capital-gain', 'capital-loss', 'hours-per-week']
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # How many of each race are represented in this dataset?
    race_count = df['race'].value_counts()

    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    total_people = len(df)
    bachelors_count = len(df[df['education'] == 'Bachelors'])
    percentage_bachelors = round((bachelors_count / total_people) * 100, 1)

    # What percentage of people with advanced education make more than 50K?
    advanced_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced_education]
    lower_education = df[~advanced_education]

    higher_education_rich = round(
        (len(higher_education[higher_education['salary'] == '>50K']) / len(higher_education)) * 100, 1
    )

    # What percentage of people without advanced education make more than 50K?
    lower_education_rich = round(
        (len(lower_education[lower_education['salary'] == '>50K']) / len(lower_education)) * 100, 1
    )

    # What is the minimum number of hours a person works per week?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round(
        (len(min_workers[min_workers['salary'] == '>50K']) / len(min_workers)) * 100, 1
    )

    # What country has the highest percentage of people that earn >50K?
    country_counts = df['native-country'].value_counts()
    country_rich_counts = df[df['salary'] == '>50K']['native-country'].value_counts()
    country_rich_percentage = (country_rich_counts / country_counts) * 100
    highest_earning_country = country_rich_percentage.idxmax()
    highest_earning_country_percentage = round(country_rich_percentage.max(), 1)

    # Identify the most popular occupation for those who earn >50K in India.
    india_50k = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_50k['occupation'].value_counts().idxmax()

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

