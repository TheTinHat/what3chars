
# what3chars

what3chars is a Python module that provides functions for decoding and
encoding confusing, hard to decipher characters to and from latitude
and longitude coordinates. It combines lower case and upper case 'L's,
'I's, and '1's into geospatially unique but visually indecipherable
strings. 

Example:
```
  >>> import what3chars
  >>> print 'what3chars for 42.6, -5.6:', what3chars.encode(42.6, -5.6)
  what3chars for 42.6, -5.6: LlIiILilLliIlL1LlIliIliIiIliL1l1LlIL
```
You can specify an arbitrary precision when encoding. The precision
determines the number of characters in the what3chars:
```
  >>> print 'what3chars for 42.6, -5.6:', what3chars.encode(42.6, -5.6, precision=20)
  what3chars for 42.6, -5.6: LlIiILilLliIlL1LlIliI
```
Decoding a what3chars returns a (latitude, longitude) tuple:
```
  >>> print 'Coordinate for what3chars LlIiILilLliIlL1LlIliI:', what3chars.decode('LlIiILilLliIlL1LlIliI')
  Coordinate for what3chars LlIiILilLliIlL1LlIliI: ('42.6', '-5.6')
```

## License

what3chars is free software: you can redistribute it and/or modify it
under the terms of the GNU Affero General Public License as published
by the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

what3chars is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Affero General Public
License for more details.

You should have received a copy of the GNU Affero General Public
License along with Geohash.  If not, see
<http://www.gnu.org/licenses/>.

This is a fork of https://github.com/vinsci/geohash

## History


This is a parody of a popular geolocation system, and the code is a fork of 
Geohash by Leonard Norrgard. The only real changes are to replace the base32
pool of characters with combinations of indecipherable letters.

