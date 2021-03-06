# -*- coding: utf-8 -*-
#
# This file is part of CERN Document Server.
# Copyright (C) 2016 CERN.
#
# CERN Document Server is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# CERN Document Server is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with CERN Document Server; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Test cds-dojson CLI and jsonschema compiler."""

from __future__ import absolute_import

import json
import pkg_resources
from click.testing import CliRunner

from cds_dojson.cli import compile_schema


def test_cli():
    """Test cds-dojson CLI."""
    runner = CliRunner()
    result = runner.invoke(
        compile_schema,
        [pkg_resources.resource_filename(
            'cds_dojson.schemas', 'records/video_src-v1.0.0.json'), ]
    )

    assert 0 == result.exit_code
    compiled_schema_result = json.loads(result.output)
    with open(pkg_resources.resource_filename(
            'cds_dojson.schemas', 'records/video-v1.0.0.json'), 'r') as f:
        compile_schema_expected = json.load(f)
    assert compile_schema_expected == compiled_schema_result

    result = runner.invoke(
        compile_schema,
        [pkg_resources.resource_filename(
            'cds_dojson.schemas', 'records/project_src-v1.0.0.json'), ]
    )

    assert 0 == result.exit_code
    compiled_schema_result = json.loads(result.output)
    with open(pkg_resources.resource_filename(
            'cds_dojson.schemas', 'records/project-v1.0.0.json'), 'r') as f:
        compile_schema_expected = json.load(f)
    assert compile_schema_expected == compiled_schema_result
