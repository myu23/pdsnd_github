import time
import pandas as pd
import numpy as np


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
WEEKDAY = ['sunday', 'monday', 'tuesday', 'thursday', 'friday', 'saturday', 'sunday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
    city = city.lower()
    while city not in CITY_DATA:
        print('\nInput is invalid, please enter again!')
        city = input('Would you like to see data for Chicago, New York City, or Washington?\n')
        city = city.lower()
    print()
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input('Which month would you like to filter - January, February, March, April, May, June, or All?\n')
    month = month.lower()
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print('\nInput is invalid, please enter again!')
        month = input('Which month would you like to filter - January, February, March, April, May, June, or All?\n')
        month = month.lower()

    print()
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('Which day of the week would you like to filter - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All?\n')
    day = day.lower()
    while day not in ['all','sunday', 'monday', 'tuesday', 'thursday', 'friday', 'saturday', 'sunday']:
        print('\nInput is invalid, please enter again!')
        day = input('Which day of the week would you like to filter - Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or All?\n')
        day = day.lower()

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])


    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe

        df = df[df['day_of_week'] == WEEKDAY.index(day)]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    print("\nThe most common month is {}.\n".format(months[df['month'].mode()[0]-1].title()))

    # TO DO: display the most common day of week
    print("\nThe most common day of week is {}.\n".format(WEEKDAY[df['day_of_week'].mode()[0]]))


    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("\nThe most common start hour is {}.\n".format(df['hour'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('\nThe most commonly used start station is {}.'.format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print('\nThe most commonly used end station is {}.'.format(df['End Station'].mode()[0]))


    # TO DO: display most frequent combination of start station and end station trip
    df['Station Pair'] = 'from '+ df['Start Station'] + ' to ' + df['End Station']
    print('\nThe most frequent combination of start and end station trip is {}.'.format(df['Station Pair'].mode()[0]))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('\nTotal travel time is {}.\n'.format(df['Trip Duration'].sum()))


    # TO DO: display mean travel time
    print('\nTotal travel time is {}.\n'.format(df['Trip Duration'].mean()))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print('\nCounts of user types:')
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    # no gender and birth year info provided in data
    if 'Gender' in df.columns:
        print('\nCounts of gender:')
        print(df['Gender'].value_counts())
    else:
        print('Gender information is not provided in the original data!\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns:
        print('\nThe earliest year of birth is {}.\n'.format(int(df['Birth Year'].min())))
        print('\nThe most recent year of birth is {}.\n'.format(int(df['Birth Year'].max())))
        print('\nThe most common year of birth is {}.\n'.format(int(df['Birth Year'].mode()[0])))
    else:
        print('Birth year information is not provided in the original data!\n')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def raw_data(df):
    """Ask if user want to see raw data"""

    see_raw = input('\nWould you like to see the raw data? (Yes or No)\n').lower()
    while see_raw not in ('yes','no'):
        print('\nInvalid input!\n')
        see_raw = input('\nWould you like to see the raw data? (Yes or No)\n').lower()

    start = 0
    while see_raw == 'yes' and start < df.size:
        print(df.iloc[start:start+5,:])
        start += 5
        see_raw = input('\nWould you like to see another 5 lines? Yes or No\n').lower()
        while see_raw not in ('yes', 'no'):
            print('\nInvalid input!\n')
            see_raw = input('\nWould you like to see another 5 lines? Yes or No\n').lower()

    if(start >= df.size):
        print('You have reached to the end of the raw data. End.')

    return





def main():
    """execute the script when this script is main script"""
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)

        #no user
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

def test():
    """test functions"""
    df = load_data('chicago', 'all', 'all')
    raw_data(df)
    time_stats(df)
    station_stats(df)
    trip_duration_stats(df)
    user_stats(df)

if __name__ == "__main__":
	main()
