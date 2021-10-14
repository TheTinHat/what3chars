"""
what3chars is a fork of Geohash produced by Leonard Norrgard under 
the GNU Affero General Public License (original notice below). It is 
meant only as parody of a popular but problematic geolocational app. 
Do not actually use it.

And please, do not sue me. This was for fun :)

---------------------------------------------------------------
Copyright (C) 2008 Leonard Norrgard <leonard.norrgard@gmail.com>
Copyright (C) 2015 Leonard Norrgard <leonard.norrgard@gmail.com>

This file is part of what3chars.

what3chars is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

what3chars is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public
License along with what3chars.  If not, see
<http://www.gnu.org/licenses/>.
"""
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name = "what3chars",
    version = "1.0.2",
    packages = find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    # metadata for upload to PyPI
    author = "David Swanlund",
    author_email = "david.swanlund@gmail.com",
    description = "Module to decode/encode indecipherable and confusing characters to/from latitude and longitude.",
    license = "GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.",
    keywords = "Geohash What3Chars",
)
