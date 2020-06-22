# whatsapp-bot
WhatsApp Bot to send a message to multiple numbers without adding them as a contact.

## Requirements
1. Selenium
```python
pip install selenium
```
2. [Selenium Drivers](https://selenium-python.readthedocs.io/installation.html#drivers)
PS- Change the driver code according to your web browser.

## How to use
1. Add all the numbers in the **numbers.txt**.
  The phone numbers should be on a new line and **must** have the country code **without** "**+**" or **0**
2. Paste in the message in the **message.txt** file. 
    **Chromedriver does not support emojis, use firefox instead**
3. Run **whatsapp-bot.py**
