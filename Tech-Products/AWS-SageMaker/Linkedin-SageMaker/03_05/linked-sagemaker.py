import os
import boto3
import json
from datetime import datetime

# grab environment variables
ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
DEEPLENS_DEVICE_NAME = os.environ['DEEPLENS_DEVICE_NAME']
runtime = boto3.Session().client(service_name='sagemaker-runtime', region_name='us-east-1')
rekognition = boto3.client('rekognition')
s3 = boto3.client('s3')
sns = boto3.client('sns')


def lambda_handler(event, context):
    # parse the trigger event for the bucket name and object key (i.e. image file name)
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    # retrieve the object/image file
    image = {
        'S3Object': {
            'Bucket': bucket,
            'Name': key,
        }
    }

    # send the image to the Rekognition service to retrieve attributes about the person
    response = rekognition.detect_faces(Image=image, Attributes=['ALL'])

    # get AverageAge from picture
    average_age = str(
        int((response['FaceDetails'][0]['AgeRange']['Low'] + response['FaceDetails'][0]['AgeRange']['High']) / 2))

    # get Gender from picture
    gender = convert_gender(response['FaceDetails'][0]['Gender']['Value'])

    # get current month
    currentMonth = str(datetime.now().month)

    # get day of the week
    currentWeekDay = determine_day_of_week(datetime.now().weekday())

    # get time of day
    currentTimeofDay = convert_time_of_day(determine_time_of_day())

    # retrieve values needed to invoke the SageMaker model to retrieve a crime prediction
    # Real Test Values:
    # payload = "3,1,30,0,1,0,1,0,0,0,0,0,1,0,0" #row 1 data points from "test.csv", excludes first target (i.e. first column) - No Crime
    # payload = "2,6,21,0,1,0,1,0,0,0,0,1,0,0,0" #row 1 data points from "test.csv", excludes first target (i.e. first column) - Crime
    # payload = "1,3,21,0,1,0,0,1,0,0,0,1,0,0,0" #row 2107 data points from "test.csv", excludes first target (i.e. first column) - No Crime
    # payload = "4,10,30,0,1,1,0,0,0,0,0,0,0,1,0" #row 2109 data points from "test.csv", excludes first target (i.e. first column) - Crime

    payload = create_payload(DEEPLENS_DEVICE_NAME, average_age + ",", gender, currentMonth + ",", currentTimeofDay,
                             currentWeekDay)
    print(payload)

    response = runtime.invoke_endpoint(EndpointName=ENDPOINT_NAME,
                                       ContentType='text/csv',
                                       Body=payload)
    print("********Response*******")
    print(response)
    print("********End Response***")
    result = json.loads(response['Body'].read().decode())
    print("********Result*********")
    print(result)
    print("*******End Result******")
    print("*******Prediction******")
    prediction = int(result['predictions'][0]['predicted_label'])
    print(prediction)
    print("*******End Prediction***")
    print("*******Confidence*******")
    confidence_score = "{:.2%}".format(result['predictions'][0]['score'])
    print(confidence_score)
    print("*******End Confidence***")

    predicted_label = 'Crime' if prediction == 1 else 'No Crime'
    publish_message(predicted_label)

    return predicted_label


def create_payload(camera_location, age, gender, month, time_of_day, day_of_week):
    # values needed by model (all must be in numeric format):

    # DayofWeek,Month,AverageAge,Gender_Female,Gender_Male,TimeofDay_afternoon, TimeofDay_evening,
    # TimeofDay_morning,County_DevonCornwall,County_Dorset,County_Essex,County_Hampshire,County_Kent,
    # County_Nottinghamshire,County_Surrey
    # 4,10,30,0,1,1,0,0,0,0,0,0,0,1,0
    payload = str(day_of_week) + str(month) + str(age) + gender + str(time_of_day) + str(
        convert_camera_location(camera_location))

    return payload


def convert_camera_location(location):
    # take Surrey_Camera and convert to County_DevonCornwall,County_Dorset,County_Essex,County_Hampshire,County_Kent,
    # County_Nottinghamshire,County_Surrey (where County_Surrey has a 1 and all other counties have a 0)
    if location == 'Surrey_Camera':
        return "0,0,0,0,0,0,1"
    elif location == 'DevonCornwall_Camera':
        return "1,0,0,0,0,0,0"
    elif location == 'Dorset_Camera':
        return "0,1,0,0,0,0,0"
    elif location == 'Essex_Camera':
        return "0,0,1,0,0,0,0"
    elif location == 'Hampshire_Camera':
        return "0,0,0,1,0,0,0"
    elif location == 'Kent_Camera':
        return "0,0,0,0,1,0,0"
    elif location == 'Nottinghamshire_Camera':
        return "0,0,0,0,0,1,0"


def convert_gender(gender):
    # take Male or Female and convert to Gender_Female,Gender_Male
    if gender == 'Male':
        return "0,1,"
    else:  # Female
        return "1,0,"


def convert_time_of_day(time_of_day):
    # take Morning, Afternoon, Evening and convert to TimeofDay_afternoon, TimeofDay_evening, or TimeofDay_morning
    if time_of_day == 'Morning':
        return "0,0,1,"
    elif time_of_day == 'Afternoon':
        return "1,0,0,"
    elif time_of_day == 'Evening':
        return "0,1,0,"


def determine_day_of_week(day):
    # In Python - Monday is 0 and Sunday is 6
    # For Training Data - Monday is 1 and Sunday is 7
    if day == 0:
        return "1,"
    elif day == 1:
        return "2,"
    elif day == 2:
        return "3,"
    elif day == 3:
        return "4,"
    elif day == 4:
        return "5,"
    elif day == 5:
        return "6,"
    elif day == 6:
        return "7,"


def determine_time_of_day():
    # python uses 24 hour clock - range(24)
    morning = ["5", "6", "7", "8", "9", "10", "11", "12"]
    afternoon = ["13", "14", "15", "16", "17"]
    evening = ["18", "19", "20", "21", "22", "23", "0", "1", "2", "3", "4"]
    hour = str(datetime.now().hour)

    if hour in morning:
        return 'Morning'
    elif hour in afternoon:
        return 'Afternoon'
    elif hour in evening:
        return 'Evening'
    else:
        return 'error'


def publish_message(prediction):
    print(prediction)
    sns.publish(
        TopicArn='arn:aws:sns:us-east-1:241215432415:sagemaker-crime-alert',
        Message=json.dumps(DEEPLENS_DEVICE_NAME + " has detected a person. The prediction is : " + prediction),
        MessageStructure='string',
        MessageAttributes={
            'summary': {
                'StringValue': 'Crime Prediction',
                'DataType': 'String'
            }
        }
    )
