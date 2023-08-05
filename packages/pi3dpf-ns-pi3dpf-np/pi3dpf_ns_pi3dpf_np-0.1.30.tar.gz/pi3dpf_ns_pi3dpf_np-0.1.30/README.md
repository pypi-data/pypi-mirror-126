# Alexa now playing configuration instructions #

## resolving login problems ##

    INFO: alexa - alexa login failed. If the problem persists, open /home/pi/.pf/logs/alexa_response.html in browser, delete cookies and login
If you see this message in the log, please login to your Alexa account from the same machine you have the now-playing daemon running.
In most of the cases, a captcha is provided and once this is done, the daemon can be started without problem.

Keep in mind that there are several URLs used by amazon for authenticating their clients.
Set the property PI3D_ALEXA_ACCOUNT_BASE_URL accordingly in /home/pi/.pf/pf.config: 

    PI3D_ALEXA_ACCOUNT_BASE_URL   : https://alexa.amazon.de  # Germany
    PI3D_ALEXA_ACCOUNT_BASE_URL   : https://alexa.amazon.com # the rest of the world



## How to get PI3D_RADIOTIME_PARTNER_ID ##
If you browse in Chrome or Edge to the page https://alexa.amazon.de/spa/index.html#music/TUNE_IN, and then
continue to Favorites, the link will extend to something like this:
https://alexa.amazon.de/spa/index.html#music/TUNE_IN/link/aHR0cDovL29wbWwucmFkaW90aW1lLmNvbS9Ccm93c2UuYXNoeD9jPXByZXNldHMmZm9ybWF0cz1hYWMsbXAzJnBhcnRuZXJJZD0hRWFhYWFhYSZzZXJpYWw9QXh4eHh4eHh4eHh4eHh4eHh4eHh4eHh4eCZsb2NhbGU9ZW4mbGF0bG9uPTM0LjUxMDQ5MCwtODUuMzEyMTExCg
which is base64 encoded. 

Using 'echo aHR0cDovL29wb...| base64 -d', the data-url provides:
http://opml.radiotime.com/Browse.ashx?c=presets&formats=aac,mp3&partnerId=!Eaaaaaa&serial=Axxxxxxxxxxxxxxxxxxxxxxxx&locale=en&latlon=34.510490,-85.312111


    echo aHR0cDovL29wb...| base64 -d
    http://opml.radiotime.com/Browse.ashx?c=presets&formats=aac,mp3&partnerId=!Eaaaaaa&serial=Axxxxxxxxxxxxxxxxxxxxxxxx&locale=en&latlon=34.510490,-85.312111

Remarks: adding &render=json to the url will return JSON.

    add the following line to your config file /home/pi/.pf/pf_secrets:
    radio_time_partner_id: !Eaaaaaa

