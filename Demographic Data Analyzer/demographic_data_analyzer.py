import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    #QUESTION #1
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()


    #QUESTION 2
    # What is the average age of men?
    average_age_men = df['age'][df['sex'] == 'Male'].mean()
    average_age_men = round(average_age_men, 1)

  
    #QUESTION 3
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = df['education'][df['education'] == 'Bachelors'].count()/df['education'].count() * 100
    percentage_bachelors = round(percentage_bachelors, 1)


    #QUESTION 4
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?

    # All people with either a Bachelors, Masters or Doctorate Degree
    higher_education = df[(df['education'] == 'Bachelors') | (df['education'] == 'Masters') | (df['education'] == 'Doctorate')]
    
    # Higher educated people who also make more than $50K
    h_ed_over50 = higher_education[higher_education['salary'] == '>50K']
    
    # Percent of higher educated who make more than $50K
    higher_education_rich = round(len(h_ed_over50)/len(higher_education) * 100, 1)

    # What percentage of people without advanced education make more than 50K?
    
    # All people without a Bachelors, Masters or Doctorate Degree
    lower_education = df[(df['education'] != 'Bachelors') & (df['education'] != 'Masters') & (df['education'] != 'Doctorate')]
    
    # Lower educated people who also make more than $50K
    l_ed_over50 = lower_education[lower_education['salary'] == '>50K']
    
    # Percent of lower educated who make more than $50K
    lower_education_rich = round(len(l_ed_over50)/len(lower_education) * 100, 1)


    #QUESTION 5 
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()


    #QUESTION 6
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    
    # Total qty of workers who work the minimum hours/week
    num_min_workers = len(df[df['hours-per-week'] == min_work_hours])
    
    # Workers who work the minimum hours/week and make more than $50K
    min_workers_rich = df[(df['hours-per-week'] == min_work_hours) & (df['salary'] == '>50K')]
    
    # Percentage of minimum hours/week workers who make more than $50K
    rich_percentage = round(len(min_workers_rich)/num_min_workers * 100, 1)


    #QUESTION 7
    # What country has the highest percentage of people that earn >50K and what is that percentage?
    
    # Total qty of workers/country
    all_country_counts = df['native-country'].value_counts()
    
    # All workers who earn more than $50K
    over_50K = df[df['salary'] == '>50K']
    
    # Countries (and qty of occurences) of workers who earn more than $50K
    over_50_country_counts = over_50K['native-country'].value_counts()
    
    # Percentage of workers earning over $50K, by country
    over_50_country_percents = (over_50_country_counts/all_country_counts).sort_values(ascending=False)
    
    # Country with highest percentage of its workers earning over $50K
    highest_earning_country = over_50_country_percents.index[0]
    
    # Percentage of workers earning more than $50K who are native to top country
    highest_earning_country_percentage = round(over_50_country_percents[highest_earning_country] * 100, 1)


    #QUESTION 8
    # Identify the most popular occupation for those who earn >50K in India.
    
    # All workers from India earning more than $50K
    india_df = df[(df['native-country'] == "India") & (df['salary'] == ">50K")]
    
    # Most common occupation for Indians earning more than $50K
    top_IN_occupation = india_df['occupation'].value_counts().index[0]

  
    # DO NOT MODIFY BELOW THIS LINE

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
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
