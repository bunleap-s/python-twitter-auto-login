# python-twitter-auto-login
This project used Selenium as function to control the browser and check for HTML name attributes and input in information then login to Twitter automatically.

## Instructions
We need to import `selenium` in order to get this to work.
Make sure to check your `pip` version in this directory 
```
C:\Python27\Scripts
```
to know what version you have or using.

### Install Selenium
```
pip install selenium
```

### Install WebBrowser Drivers
A lot of developers are using different kinds of browsers. Download the browser driver.

[Chrome](https://www.google.com), [Firefox](https://www.google.com), [Edge](https://www.google.com), [Safari](https://www.google.com)

After downloading, just extract it and put it this directory.
```
C:\Python27\Scripts
```

### Test WebDriver
In your Console or Terminal, type `python apps.py` to start the browser and perform the action.
We do this to check if the driver is working or not.

### Changing Email & Password
After everything work just edit this two line and start the app again using `python apps.py`
```python
#Put in Email
email.send_keys('example@company.com')

#Put in Password
password.send_keys('Pa$$w0rd')
```
