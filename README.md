What is File Static?
====================
File Static is a very small and simply python script, that doing some actions when some events are triggered. For example you can configure script to remove certain file if it was created every second.

---

Configuration
=============
Option           | Type    | Description
-----------------|---------|------------
files            | string  | files for processing (can be separated by space)
additional files | string  | additional file(s), using for _modify_ event and _copy_ action
event_type       | string  | type of event: _modify_, _create_, _remove_ or _modify/remove_
action           | string  | action with file when the event is trigerred: _copy_ or _remove_
interval         | float   | interval between event check, in seconds
loop             | boolean | if _true_ - exit after first performed action, if false - checks the event forever
