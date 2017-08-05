File Static
===========
  * [What is File Static?](#what-is-file-static?)
  * [Configuration](#configuration)
  * [Files](#files)
  * [Event types](#event-types)
  * [Actions](#actions)

---

What is File Static?
====================
File Static is a very small and simply python script, that doing some actions when some events are triggered.
For example you can configure script to remove certain file if it was created every second.

---

Configuration
=============
Option           | Type    | Description
-----------------|---------|------------
files            | string  | files for processing (can be separated by space)
additional_files | string  | additional file(s), using for `modify` event and `copy` action
event_type       | string  | type of event: `modify`, `create`, `remove` or `modify/remove`
action           | string  | action with file when the event is trigerred: `copy` or `remove`
interval         | float   | interval between event check, in seconds
loop             | boolean | if `true` - exit after first performed action, if false - checks the event forever

---

Files
=====
File Static supports both single file and multiple files for processing.

To specify multiple files separate there with space. If file name contains spaces - enclose the file name in doublequotes.  
Example:
`files = "File 1.txt" "File 2.txt" "File 3.txt"`

You can also specify multiple additional files if you specified multiple files for processing.
If count of `additional_files` is less than count of `files` - first additional file would be applied to all `files`.

For example: if count of `additional_files` is count of `files`, script would be work like this:
> file1 --> additional_file1  
> file2 --> additional_file2  
> file3 --> additional_file3

But if count of `additional_files` is less then count of `files`, script would be work like this:
> file1 --> additional_file1  
> file2 --> additional_file1  
> file3 --> additional_file1

---

Event types
===========
There is 4 event types, they triggering when one of the files specified in `files` option was:

  * `modify` - modified, using `additional_files` option to compare with `file`
  * `create` - created
  * `remove` - removed
  * `modify/remove` - modified or removed

---

Actions
=======
There is 2 posible actions:

  * `copy` - copy `additional_files` to `files` with overwriting
  * `remove` - remove the `files`