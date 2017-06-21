# Pushbullet Integration Pack

StackStorm integration with [Pushbullet](https://www.pushbullet.com) messaging application.

## Configuration

Copy the example configuration in [pushbullet.yaml.example](./pushbullet.yaml.example)
to `/opt/stackstorm/configs/pushbullet.yaml` and edit as required.

It should contain:

* ``apikey`` - Pushbullet API Key

You can also use dynamic values from the datastore. See the
[docs](https://docs.stackstorm.com/reference/pack_configs.html) for more info.

**Note** : When modifying the configuration in `/opt/stackstorm/configs/` please
           remember to tell StackStorm to load these new values by running
           `st2ctl reload --register-configs`

## Actions

* ``post_to_channel`` - Post a message to a channel. Provide a channel, message and optionally a subject
