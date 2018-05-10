# Documentaion

## Device to server API:

### Submit status

#### Endpoint: submit_status/

Requires the request method to be POST and the MIME type to be form encoded.
The request must have the form id=\<integer\>&status=\<integer\>&time=\<unixtime\>

Special case: when status is set to 0 the server doesn't record anything. This is so the device
has access to a timestamp for synchronization.

Status Codes:
- 1: Malfunction detected
- 2: Intervention required
- 3: Operating correctly
- 4: Requires action from operator
- 5: Requires constant action from operator