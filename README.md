
# iOSPushNotification
Send notification for iOS with Firebase in Python

Use this code to send push notification to specific or group iOS device(s).

## Installation

 1. `    pip3 install requests`
 2.  add `app_key` and `device_token` from Firebase

## Usage
For normal notification:

    notification = PushNotification()
    notification.send('Title', 'Body')

With subtitle:

    notification = PushNotification()
    notification.sendWithSubtitle('Title', 'Subtitle', 'Body')

Without sound:

    notification = PushNotification()
    notification.sendWithoutSound('Title', 'Body')

Enjoy 🙂
