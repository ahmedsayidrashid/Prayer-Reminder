# MAINTAINERS GUIDE

## Prayer API Usage

This guide provides instructions for maintainers and developers on how to use the Adhan (Prayer Times) API and more.

## API Implementation

To get familiar with the API, I am using `curl` to get raw HTTP response from the endpoint.

For example, if I want to get the prayer times for today, I'd use the following curl command.

```sh
curl -s 'https://api.aladhan.com/v1/timingsByAddress/04-10-2025?address=Canada,Ottowa&method=1'
```

The command above gets the prayer times for October 4th, 2025 in Ottawa, Canada.

Since the response is a JSON message that's poorly formatted, I pipe the result of this command to a JSON formatter via `jq`

```sh
curl -s 'https://api.aladhan.com/v1/timingsByAddress/04-10-2025?address=Canada,Ottowa&method=1' | jq
```

To install this tool on your distribution, reference your package manager, for me I use a regular Ubunutu, therefore `sudo apt install jq` works fine.
