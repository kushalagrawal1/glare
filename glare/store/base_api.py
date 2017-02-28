# Copyright 2017 OpenStack Foundation.
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.


class BaseStoreAPI(object):

    def add_to_backend(self, context, blob_id, data, verifier=None):
        """Save data to database store type and return location info

        :param blob_id: id of artifact
        :param data: file iterator
        :param context: user context
        :param verifier:signature verified
        :return: database location uri
        """
        raise NotImplementedError()

    def get_from_store(self, uri, context):
        """Load file from database store

        :param uri: blob uri
        :param context: user context
        :return: file iterator
        """
        raise NotImplementedError()

    def delete_from_store(self, uri, context):
        """Delete blob from database store

        :param uri: blob uri
        :param context: user context
        """
        raise NotImplementedError()