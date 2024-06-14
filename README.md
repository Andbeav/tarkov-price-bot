# tarkov-price-bot

A twitch bot for fetching the last low price of an item from the [tarkov.dev graphql service](https://tarkov.dev/api/).

## Running the bot

Fill in the missing config in the `.env` file.

* `ACCESS_TOKEN` You can generate a chatbot token with just read/write access using [this site](https://twitchtokengenerator.com/).
* `CHANNEL_NAME` The name of your twitch channel (not your full url)
* `COMMAND_PREFIX` The symbol used before the command (defaults to `!` i.e. `!p wires`)

Run using podman (or docker) compose: `podman-compose run --rm app`
