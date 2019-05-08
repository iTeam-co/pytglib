Python-Telegram
===============

   Welcome to Python-Telegram! Python-Telegram is a python wrapper for
   Tdlib, completely Object-Oriented and originally based on Tdlib’s
   suggested libs for python.

Installation
============

Installing the library is super easy. First, be sure to have Python3
installed in your server: ``apt install python3``

Then, simply execute the installation script: ``python3 setup.py install``

And you’re ready to go!

A simple script
===============

Here’s a simple script that prints every update it receives from
Telegram:

::

   from pytglib.client import Telegram

   # Change the values below
   api_id = 7
   api_hash = '123412341234123412341234'
   phone_number = '+12312312312'
   dbenc = '32_hexademical_chars'

   # Initiate the client
   client = Telegram(api_id=api_id, api_hash=api_hash, phone=phone_number, database_encryption_key=dbenc)

   # Login to the client
   client.login() 

   # Define the handler function
   def my_message_handler(update):
       print(update)

   # Register it
   client.add_message_handler(my_message_handler)

   tg.idle()

   # And you're ready to go!

For more complex scripts, go to the Examples section below:

Examples
==========================

You can find more examples in examples tree on GitHub page `here
<https://github.com/iTeam-co/Python-Telegram>`_

Documents
===============

Documents are available on `this page
<https://pytelegram.readthedocs.io/en/latest/pytglib.html>`_
