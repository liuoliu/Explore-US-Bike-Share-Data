
# coding: utf-8

# In[102]:


# %load bikeshare_2.py
import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }



# In[217]:


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    while True:
        print('Please choose from one of the following cities: Chicago, New York City, Washington')
        city=input()
        city=city.lower()
        if city in ("chicago","new york city","washington"):
            break
        else:
            True 
    
    # get user input for month (all, january, february, ... , june)

    while True:
        print("Please give the months you want to explore. Choose from January, February, March, April, May, June, July, August, September, October, November, December. Type 'ALL' 'if' you want to see 'all' the months")
        
        month=input()
        if month.lower()in ("january", 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december', 'all'):
            break
        else:
            True 

    # get user input for day of week (all, monday, tuesday, ... sunday)
    
    while True:
        print("Please give the day of week you want to explore. Choose from Monday, Tuesday, Wednesday, Thursday, Friday, Saturday and Sunday. Type 'ALL' 'if' you want to see 'all' the days" )
        
        day=input()
        if day.lower()in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday','all'):
            break
        else:
            True 

    print('-'*40)
    return city, month, day




# In[228]:


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
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.weekday_name
    
    month=month.lower()
    
    if month!='all':
        months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','december']
        month = months.index(month) + 1
        df = df[df['month'] == month] 
    
    day=day.lower()
    
    if day!='all':
        df=df[df['day']==day.title()]
    
    return df
    


# In[179]:


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    
    
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df1['Start Time'].dt.month
    popular_month=df['month'].mode()[0]
    
    import calender 
    popular_month=calendar.month_name[popular_month]
    
    print('The most common month to travel is:', popular_month)

    # display the most common day of week
    
    popular_day_of_week= df['day'].mode()[0]
    print('The most common day of week to travel is:', popular_day_of_week)
    
    # display the most common start hour

    df['hour']=df['Start Time'].dt.hour
    popular_hour=df['hour'].mode()[0]
    print('The most common hour to travel is:', popular_hour)
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# In[180]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('The most commonly used start station is:', df['Start Station'].mode()[0])
    

    # display most commonly used end station

    print('The most commonly used end station is:', df['End Station'].mode()[0])
    
    # display most frequent combination of start station and end station trip

    df['Start End Station']=df['Start Station']+df['End Station']
    
    print('The most commonly used combination of start and end station trip is:', df['Start End Station'].mode()[0])
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# In[181]:


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    
    
    df['End Time']=pd.to_datetime(df['End Time'])
    df['duration']=df['End Time']-df['Start Time']
    print('The total travel time is:',df['duration'].sum())
    
    # display mean travel time

    print('The average travel time is:',df['duration'].mean())
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




# In[206]:


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    
    
    print('The counts of user types are:', df['User Type'].value_counts())
    

    # Display counts of gender
    
    try:
        print('The counts of gender are:', df['Gender'].value_counts())
    except KeyError:
        print('No Gender information avaiable')
        pass
        
     

    # Display earliest, most recent, and most common year of birth
    
    try:
        print('The youngest user was born:', df['Birth Year'].max())
    except KeyError:
        print('No Birth Year information avaiable')
        pass
    
    try:
        print('The oldest user was born:', df['Birth Year'].min())
    except KeyError:
        pass
    
    try:
        print('The most common user year of birth is ', df['Birth Year'].mode()[0])
    except KeyError:
        pass
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    
    
    
    
    print('-'*40)




# In[236]:


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



# In[237]:



if __name__ == "__main__":
	main()


# In[ ]:




