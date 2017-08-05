What is File Static?
====================
File Static is a very small and simply python script, that doing some actions when some events are triggered.
For example you can configure script to remove certain file if it was created every second.

---

Configuration
=============
Option           | Type    | Description
-----------------|---------|------------
files            | string  | file(s) for processing (can be separated by space)
additional_files | string  | additional file(s), using in _modify_ event and _copy_ action
event_type       | string  | type of event: _modify_, _create_, _remove_ or _modify/remove_
action           | string  | action with file when the event is trigerred: _copy_ or _remove_
interval         | float   | interval between event check in seconds
loop             | boolean | if _true_ - exit after first performed action, if false - check the event forever

---

Files
=====
File Static supports both single file and multiple files for processing.

To specify multiple files separate their with space. If file name contains spaces - enclose the file name in doublequotes.  
Example:
`files = "File 1.txt" "File 2.txt" "File 3.txt"`

You can also specify multiple additional files if you specified multiple files for processing.
If count of _additional_files_ is less than count of _files_ - first additional file would be applied to all _files_.

For example: if count of _additional_files_ is count of _files_, File Static would be work like this:
> file1 --> additional_file1  
> file2 --> additional_file2  
> file3 --> additional_file3

But if count of _additional_files_ is less then count of _files_, File Static would be work like this:
> file1 --> additional_file1  
> file2 --> additional_file1  
> file3 --> additional_file1

---

Event types
===========
There is 4 event types, they triggering when one of the _files_ was:

  * _modify_ - modified, using _additional_files_ option to compare with _file_
  * _create_ - created
  * _remove_ - removed
  * _modify/remove_ - modified or removed

---

Actions
=======
There is 2 posible actions:

  * _copy_ - replace one of the _files_, that triggered the event with _additional_files_
  * _remove_ - remove one of the _files_, that triggered the event