
import pandas as pd
netflix_data= pd.read_csv("C:\\Users\\claud\\Downloads\\netflix-report.zip\\CONTENT_INTERACTION")
netflix_data
netflix_data.shape
netflix_data.head(1)
netflix_data = netflix_data.drop(['Profile Name', 'Attributes', 'Supplemental Video Type', 'Device Type', 'Bookmark', 'Latest Bookmark', 'Country'], axis=1)
netflix_data.head(1)
netflix_data.dtypes
netflix_data['Start Time'] = pd.to_datetime(df['Start Time'], utc=True)
netflix_data.dtypes
netflix_data = netflix_data.set_index('Start Time')
netflix_data.index = netflix_data.index.tz_convert('US/Eastern')
netflix_data = netflix_data.reset_index()
netflix_data.head(1)
netflix_data['Duration'] = pd.to_timedelta(netflix_data['Duration'])
netflix_data.dtypes
netflix_data = netflix_data[netflix_data['Title'].str.contains('The Office (U.S.)', regex=False)]
office.shape
office['Duration'].sum()
office['weekday']=office['Start Time'].dt.weekday
office['hour']=office['Start Time'].dt.hour
import matplotlib
office['weekday'] = pd.Categorical(office['weekday'], categories=
    [0,1,2,3,4,5,6],
    ordered=True)
office_by_day = office['weekday'].value_counts()

office_by_day = office_by_day.sort_index()

matplotlib.rcParams.update({'font.size': 22})

office_by_day.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Day')

office['hour'] = pd.Categorical(office['hour'], categories=
    [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23],
    ordered=True)

office_by_hour = office['hour'].value_counts()

office_by_hour = office_by_hour.sort_index()

office_by_hour.plot(kind='bar', figsize=(20,10), title='Office Episodes Watched by Hour')