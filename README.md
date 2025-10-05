# Prayer-Reminder

A simple application to remind prayers and track progress

## End goal

Be able to remind people when its time to pray.

This project uses a REST API to get prayer times, compares them to local times, and stores all 5 prayers in a list.

Once the current time reaches the prayer time, it reminds users that its time to pray.

The means of reminding users are different, initially, I'd like it to remind me via SMS or notication. But, because I love hardware, I'll involve hardware first.

I'll use GPIOs and a PI 5 to send a high to a GPIO once a prayer time changes.

Since it uses local time to determine if it reached prayer times, I can test if things are working as expected via a `timedatectl` change time command to see if LEDs go off as expected.

Once reminder comes, users are expected to press a pyhsical button to aknowledge prayer times.

Flask or some web framework will be used to track prayer times over time.

LETS GET THIS PROJECT GOING.
