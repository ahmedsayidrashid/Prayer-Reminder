# MAINTAINERS GUIDE

## Prayer API Usage

To get familiar with the API, I am using `curl` to get raw HTTP response from the endpoint.

For example, if I want to get the prayer times for today, I'd use the following curl command.

```sh
curl -s 'https://api.aladhan.com/v1/timingsByAddress/DD-MM-YYYY?address=Canada,Ottowa&method=3'
```

The `-s` option is to silent the unnecessary (but cool) loading bar.

The command above gets the prayer time for the given day, for example `04-10-2025` will return the prayer times for October 4th, 2025 in Ottawa, Canada using the Muslim World League prayer time calculation method (standard).

Since the response is a JSON message that's poorly formatted, I pipe the result of this command to a JSON formatter via `jq`

```sh
curl -s 'https://api.aladhan.com/v1/timingsByAddress/DD-MM-YYYY?address=Canada,Ottowa&method=3' | jq
```

To install this tool on your distribution, reference your package manager, for me I use Ubuntu, therefore `sudo apt install jq` works fine.

## Connecting to a PI

Now that I've got a pretty basic setup to get the prayer times, we will integrate our PI 5 into the project

Instead of using a external display to find the IP of the PI, `nmap` is a good option to find the IP of the PI and to scan for devices on your network.

However, because I use a TP-Link range extender to get better WIFI access in my room, I can simply use the app to get the IP of the PI.

Given the the IP of the PI, install the necessary extension to develop via SSH on Vscode.

## Dependencies

To install all the dependencies of this 'package' (will be one soon eventually), run the following command.

```sh
pip install -r requirements.txt
```

The command above will install all the dependencies listed in `requirements.txt`.

Note that developers should keep the file updated by piping the result of `pip list --format=freeze` into the file.

`build.sh` updates the list of dependencies each time it runs, as well as performing linting + formatting.
