For devices connecting to the server:

API

submit_status/ : requires the request method to be POST and the MIME type to be form encoded.
The request must have the form id=\<integer\>&status=\<integer\>&time=\<unixtime\>

Special case: when status is set to 0 the server doesn't record anything. This is so the device
has access to a timestamp for synchronization.