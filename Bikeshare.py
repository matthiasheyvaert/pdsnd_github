import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    while True:
        try:
            city = input("Fill in the name of the city you would like to see the data of: chicago, new york city or washington.\n").lower()
            print("you have entered following city: {}".format(city))
            if city in CITY_DATA:
                break
            else:
                print("no data for this city, try again")
        except (Exception, KeyboardInterrupt):
            print("An error occurred, please enter city name again")


    months = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        try:
            month = input("Enter the name of the month you would like to see the data of, type all of you want to see all data: all, january, february, march, april, may, june.\n ").lower()
            print("you have entered following month: {}".format(month))
            if month in months:
                break
            else:
                print("no data available for this month, please try again")
        except (Exception, KeyboardInterrupt):
            print("An error occurred, please enter name of month again")


    days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while True:
        try:
            day = input("Enter the name of the day you would like to see the data of, type all of you want to see all data: all, monday, tuesday, wednesday, thursday, friday, saturday, sunday.\n").lower()
            print("you have entered following day: {}".format(day))
            if day in days:
                break
            else:
                print("no data available, please try again")
        except (Exception, KeyboardInterrupt):
            print("An error occurred, please enter name of month again")

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    df = pd.read_csv(CITY_DATA[city])


    df['Start Time'] = pd.to_datetime(df['Start Time'])


    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name


    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1


        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    most_common_month = df['month'].mode()[0]
    print("most common month is {}".format(most_common_month))


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['day'] = df['Start Time'].dt.day_name()
    most_common_day = df['day'].mode()[0]
    print("most common day is {}".format(most_common_day))


    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['hour'] = df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print("most common hour is {}".format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()


    Start_station = df['Start Station'].value_counts().head(1)
    print("Most common start station is \n{}".format(Start_station))


    End_station = df['End Station'].value_counts().head(1)
    print("Most common end station is \n{}".format(End_station))


    combi_start_end = df.groupby(['Start Station', 'End Station']).size().idxmax()
    print("Most frequent combination is \n {}".format(combi_start_end))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    total_duration = df['Trip Duration'].sum()
    print("total travel time is {}".format(total_duration))


    average_duration = df['Trip Duration'].mean()
    print("Average travel time is {}".format(average_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()


    user_types = df['User Type'].value_counts()
    print("the count of user types is \n{}".format(user_types))

    try:
        gender_count = df['Gender'].value_counts()
        print("the count of gender is \n{}".format(gender_count))
    except:
        print("column not available for this city")

    try:
        earliest_year_of_birth = df['Birth Year'].min()
        recent_year_of_birth = df['Birth Year'].max()
        most_common_year_of_birth = df['Birth Year'].value_counts().head(1)
        print("the earliest year of birth is {}, the most recent year of birth is {}, the most common year of birth is {}".format(earliest_year_of_birth, recent_year_of_birth, most_common_year_of_birth))
    except:
        print("column not available for this city")


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def show_raw_data(df):

    """
    Code that prompt the user a question if they want to see raw data. When answer is yes.
    Code displays 5 lines of raw data.
    Iterating these prompts and displaying the next 5 lines of raw data at each iteration.
    When answer is no or when no more data to display, stops program.
    """
    pd.set_option('display.max_columns',200)
    answer = ["yes"]
    start_num = 0
    while True:
        try:
            show_data = input("Do you want to see raw data, answer yes or no: ").lower()
            if show_data in answer:
                print(df.iloc[start_num:start_num + 5, :])
                start_num += 5
            else:
                break
        except (Exception, KeyboardInterrupt):
            print("an error occurred, please enter answer again")

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        show_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
