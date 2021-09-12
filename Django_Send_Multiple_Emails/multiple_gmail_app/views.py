from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . models import Upload_CSV
from Django_Send_Multiple_Emails.settings import EMAIL_HOST_USER, MEDIA_ROOT
from django.core.mail import send_mail
import pandas as pd
import csv
from django.http import HttpResponse

@login_required
def multiple_gmail(request):
    return render(request, 'multiple_gmail_app/index.html')

@login_required
def send_multiple_gmail(request):
    if request.method == 'POST':
        # Accessing user uploaded csv file
        csv_file = request.FILES['csv_file']
        # List of rows for downloadable csv files
        successfully_email_send, failure_email_send, all_email = [], [], []
        # Variable for Accessing user uploaded csv file from database table
        database_file = ''
        # Count of successfully send emails
        email_send_successfully = 0
        # HEADER for success csv file
        success_cols = ["Sr", "To_Username", "To_Email_Address", "Subject", "Description", "Status (Yes or No)"]
        # HEADER for failure csv file
        failure_cols = ["Sr", "To_Username", "To_Email_Address", "Subject", "Description", "Status (Yes or No)"]
        # Row numbering for downloadable csv files
        var_success, var_failure, var_all = 0, 0, 0
        # Creating new record in database table for the user uploaded csv file
        try:
            csv_document = Upload_CSV.objects.create(uploaded_csv_file=csv_file)
            csv_document.save()
            # Accessing user uploaded csv file from database table
            database_file = Upload_CSV.objects.all().order_by("-id")[0]
        except Exception as e:
            print(e)
            return render(request, 'multiple_gmail_app/index.html', context={'successfully_email_send': successfully_email_send,
            'failure_email_send' : failure_email_send})
        # Reading user uploaded csv file by using Pandas
        tmp_data=pd.read_csv(database_file.uploaded_csv_file, sep=',')
        # Total number of rows(excluding HEADER row) in the user uploaded csv file
        total_email = len(tmp_data['To_Email_Address'])
        # Sending emails 
        for i in range(0, total_email):
            to_username = tmp_data['To_Username'][i]
            to_email_address = tmp_data['To_Email_Address'][i]
            email_subject = tmp_data['Subject'][i]
            email_description = tmp_data['Description'][i]
            try:
                no_of_email = send_mail(email_subject, email_description, EMAIL_HOST_USER, [to_email_address], fail_silently = False)
                email_send_successfully += no_of_email
                var_success += 1
                var_all += 1
                successfully_email_send.append([var_success, str(to_email_address), str(email_subject), str(email_description), str(to_username), 'Yes'])
                all_email.append([var_all, str(to_email_address), str(email_subject), str(email_description), str(to_username), 'Yes'])
            except Exception as e:
                var_failure += 1
                var_all += 1
                failure_email_send.append([var_failure, str(to_email_address), str(email_subject), str(email_description), str(to_username), 'No'])
                all_email.append([var_all, str(to_email_address), str(email_subject), str(email_description), str(to_username), 'No'])
                print(e)
        # Creating temporary downloadable csv files
        with open(MEDIA_ROOT / 'views_csv/Success_Email.csv', 'w') as s:
            write = csv.writer(s)
            write.writerow(success_cols)
            write.writerows(successfully_email_send)
        with open(MEDIA_ROOT / 'views_csv/Failure_Email.csv', 'w') as f:
            write = csv.writer(f)
            write.writerow(failure_cols)
            write.writerows(failure_email_send)
        with open(MEDIA_ROOT / 'views_csv/All_Email.csv', 'w') as a:
            write = csv.writer(a)
            write.writerow(failure_cols)
            write.writerows(all_email)
        print('temporaray files created')
        context = {
            'successfully_email_send': successfully_email_send,
            'failure_email_send' : failure_email_send, 
            'email_send_successfully' : email_send_successfully, 
            'email_send_failure' : total_email - email_send_successfully,
            'total_email' : total_email
        }
        return render(request, 'multiple_gmail_app/index.html', context)

def download_all_csv(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="all.csv"'  
    writer = csv.writer(response) 
    with open(MEDIA_ROOT / 'views_csv/All_Email.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i != []:
                writer.writerow(i)
    return response

def download_success_csv(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="success.csv"'  
    writer = csv.writer(response) 
    with open(MEDIA_ROOT / 'views_csv/Success_Email.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i != []:
                writer.writerow(i)
    return response

def download_failure_csv(request):
    response = HttpResponse(content_type='text/csv')  
    response['Content-Disposition'] = 'attachment; filename="failure.csv"'  
    writer = csv.writer(response) 
    with open(MEDIA_ROOT / 'views_csv/Failure_Email.csv', 'rt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for i in csv_reader:
            if i != []:
                writer.writerow(i)
    return response