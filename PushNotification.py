import requests
import json


class PushNotification:
# add your app key and device token here.
    api_key = ''
    device_token = ''

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'key=' + api_key,
    }

    def send(self, title, body):
        # makeing notification
        body = {
            'notification': {'title': title,
                             'body': body,
                             'sound': 1
                             },
            'to':
                self.device_token,
            'priority': 'high',
            #   'data': dataPayLoad,
        }

        # sending notification
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=self.headers, data=json.dumps(body))

        # get result
        json_response = response.json()
        return f'#### Notification Result ####\nType: Normal notification\nstatus_code: {response.status_code}\nsuccess: {json_response["success"]}\nfailure: {json_response["failure"]}\n################'

    def sendWithoutSound(self, title, body):
        # makeing notification
        body = {
            'notification': {'title': title,
                             'body': body,
                             },
            'to':
                self.device_token,
            'priority': 'high',
            #   'data': dataPayLoad,
        }

        # sending notification
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=self.headers, data=json.dumps(body))

        # get result
        json_response = response.json()
        return f'#### Notification Result ####\nType: Notification without sound\nstatus_code: {response.status_code}\nsuccess: {json_response["success"]}\nfailure: {json_response["failure"]}\n################'

    def sendWithSubtitle(self, title, subtitle, body):
        # makeing notification
        body = {
            'notification': {'title': title,
                             'subtitle': subtitle,
                             'body': body,
                             'sound': 1
                             },
            'to':
                self.device_token,
            'priority': 'high',
            #   'data': dataPayLoad,
        }

        # sending notification
        response = requests.post("https://fcm.googleapis.com/fcm/send", headers=self.headers, data=json.dumps(body))

        # get result
        json_response = response.json()
        return f'#### Notification Result ####\nType: Notification with subtitle\nStatus_code: {response.status_code}\nSuccess: {json_response["success"]}\nFailure: {json_response["failure"]}\n################'

##Usage:
#notification = PushNotification()
#print(notification.send('Title', 'Body'))

### Or

#notification = PushNotification()
#print(notification.sendWithSubtitle('Title', 'Subtitle', 'Body'))

### Or

#notification = PushNotification()
#print(notification.sendWithoutSound('Title', 'Body'))
