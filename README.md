# Pushbullet Integration Pack

StackStorm integration with [Pushbullet](https://www.pushbullet.com) messaging application.

## Configuration

Copy the example configuration in [pushbullet.yaml.example](./pushbullet.yaml.example)
to `/opt/stackstorm/configs/pushbullet.yaml` and edit as required.

It should contain:

* ``apikey`` - Pushbullet API Key

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

## Actions

* ``post_to_channel`` - Post a message to a channel. Provide a channel, message and optionally a subject
