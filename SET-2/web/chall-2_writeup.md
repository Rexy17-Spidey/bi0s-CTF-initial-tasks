# Challenge: Chrome Junkie

## Category
Web Exploitation

## Objective
Examine how the server checks user roles upon connection, identify where access level is stored, and manipulate it to retrieve the flag.

## Files / Target
- Target: `https://chrome-junkie.bravesky-f669ed4c.southeastasia.azurecontainerapps.io/`

## Enumeration
1. **Cookie Analysis**: Inspected `document.cookie` and found a `session_data` cookie.
2. **Decoding**: The cookie value `eyJiYWxhbmNlIjogNTAwMDAsICJ0aWVyIjogInN0YW5kYXJkIn0=` decoded to `{"balance": 50000, "tier": "standard"}`.
3. **VIP Tier**: The application indicated that restricted items require **VIP tier**.
4. **API Investigation**: Identified `/api/items` for the store inventory and `/api/buy/<id>` for purchases.

## Tools Used
- Browser Developer Tools (Console, Network)
- `curl`
- `base64`

## Commands
```bash
# Decode cookie
echo -n "eyJiYWxhbmNlIjogNTAwMDAsICJ0aWVyIjogInN0YW5kYXJkIn0=" | base64 -d

# Buy item with modified cookie
curl -X POST -H "Cookie: session_data=eyJiYWxhbmNlIjogMTAwMDAwLCAidGllciI6ICJWSVAifQ==" https://chrome-junkie.bravesky-f669ed4c.southeastasia.azurecontainerapps.io/api/buy/apogee
```

## Solution Methodology
1. **Role Tampering**: Modified the `tier` field in the `session_data` cookie from `standard` to `VIP`.
2. **Balance Manipulation**: Increased the `balance` field in the cookie to `100000` to meet the price of the target VIP item.
3. **Exploitation**: Re-encoded the JSON as Base64 and sent a POST request to the `/api/buy/apogee` endpoint. The server validated the tampered cookie and returned the flag.

## Verified Result
- **Flag**: `bi0s{3dd13s_4r3_just_numb3rs_0n_4_scr33n}`
- **Evidence**: Stored in `evidence/request_response_log.txt`.
