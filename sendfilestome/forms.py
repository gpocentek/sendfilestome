# Copyright 2018 Gauvain Pocentek
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django import forms

from sendfilestome import models
from sendfilestome import utils


class ContainerCreateForm(forms.ModelForm):
    class Meta:
        model = models.Container
        fields = ['name', 'description', 'listable', 'requires_auth']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not utils.auth_enabled():
            self.fields.pop('requires_auth')


class SFTMFileUpload(forms.ModelForm):
    class Meta:
        model = models.SFTMFile
        fields = ['file', 'name', 'container']
        widgets = {'container': forms.HiddenInput()}
