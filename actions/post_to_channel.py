# Licensed to the StackStorm, Inc ('StackStorm') under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from st2common.runners.base_action import Action
from pushbullet import Pushbullet


class PostToChannel(Action):
    def __init__(self, config):
        self.client = Pushbullet(config['apikey'])

    def get_channel(self, channel):
        return [c for c in self.client.channels if c.channel_tag == channel][0]

    def run(self, channel, message, subject=''):
        channel = self.get_channel(channel)
        return channel.push_note(subject, message)
