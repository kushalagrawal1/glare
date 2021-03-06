# Copyright 2016 Red Hat, Inc.
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


from oslo_config import cfg

service_available_group = cfg.OptGroup(name='service_available',
                                       title='Available OpenStack Services')

ServiceAvailableGroup = [
    cfg.BoolOpt("glare",
                default=True,
                help="Whether or not glare is expected to be available")
]

artifacts_group = cfg.OptGroup(name="artifacts",
                               title='Glare Options')

ArtifactGroup = [
    cfg.StrOpt("catalog_type",
               default="artifact",
               help="Catalog type of Artifacts API"),
    cfg.StrOpt("endpoint_type",
               default="publicURL",
               choices=["publicURL", "adminURL", "internalURL"],
               help="The endpoint type for artifacts service")
]
