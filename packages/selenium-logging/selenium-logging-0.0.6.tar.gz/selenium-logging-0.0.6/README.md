Explanation on youtube: https://www.youtube.com/watch?v=b5XPHqWT94s


Logging of screenshot and messages to HTML file. Can be used with selenium, but not necessary.
How to use it:

from LoggingSelenium.LogHTML import LogHTML

LogHTML.set_log_path(r"C:\pathToFolderForLogs")
LogHTML.set_logging_level(LogHTML.INFO, use_screenshot=True)

LogHTML.screenshot("Screenshot is taken")
LogHTML.debug("Random message")
LogHTML.info("Random message")



Logging levels:
-debug
-info
-warning
-error
-critical