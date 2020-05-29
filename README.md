# HWSUK Feedback Bot

This is an extremely simple bot to react to any message posted in a specified channel with thumbs up/down emoji, to enable a rudimentary feedback mechanism.

## Deployment

On Ubuntu, clone the repo, then:

```bash
sudo apt install python3 python3-venv python3-virtualenv
venv env
source env/bin/activate
pip3 install -r requirements.txt
```

Then run the bot with the following environment variables set:

| | |
| -- | -- |
| Name | Purpose |
| DISCORD_CHANNEL_ID | The channel ID to look for messages in. |
| DISCORD_CLIENT_TOKEN | The token for the bot's user. |
| DISCORD_APPEAR_INVISIBLE | Optional, if set with _any value_ the bot will appear offline. |

The instructions can be adapted for any other Linux distro for local testing.

## Usage

There are no commands, just message the channel ID specified in `DISCORD_CHANNEL_ID` and it will react to the message.