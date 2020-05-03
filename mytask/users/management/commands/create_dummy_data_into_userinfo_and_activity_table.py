from django.core.management.base import BaseCommand
from users.models import UserInfo, ActivityPeriod


"""This command is used to insert 
   data into userInfo and ActivityPeriod table"""
class Command(BaseCommand):
    help = 'Create random users'

    def handle(self, *args, **kwargs):
        UserInfo.objects.bulk_create([UserInfo(id='QWE11RC',real_name='Amit Singh',tz='Asia/kolkata'),
                                              UserInfo(id='WQE21RC',real_name='John Wick',tz='America/New_York')])


        ActivityPeriod.objects.bulk_create([ActivityPeriod(user_id='QWE11RC', start_time='Feb 1 2020  1:33PM',  end_time='Feb 1 2020 1:54PM'),
                                            ActivityPeriod(user_id='QWE11RC', start_time='Mar 1 2020  11:11AM', end_time='Mar 1 2020 2:00PM'),
                                            ActivityPeriod(user_id='WQE21RC', start_time='Feb 1 2020  1:33PM',  end_time='Feb 1 2020 1:54PM'),
                                            ActivityPeriod(user_id='WQE21RC', start_time='Mar 1 2020  11:11AM', end_time='Mar 1 2020 2:00PM')])
        print('Data Inserted Successfully')