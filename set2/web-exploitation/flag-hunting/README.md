# Challenge: Flag Hunting

## Category
Web Exploitation

## Objective
Explore the web application and systematically inspect its various components to uncover hidden flag fragments scattered throughout the site.

## Files / Target
- Target: `https://just-another-webpage--0000004.bravestone-96395b1b.southeastasia.azurecontainerapps.io/`

## Enumeration
1. **Source Code**: Found Part 1 in an HTML comment at the end of the root page.
2. **CSS Analysis**: Found Part 2 in a comment at the end of `style.css`.
3. **Directory Listing**: Accessed `/files/` and found `Part-3.jpg` containing the third fragment.
4. **HTTP Headers**: Found `part-4` in the response headers of the root page.
5. **Robots.txt**: Discovered `/itshallbedone.html`, which contained Part 5.
6. **Redirects**: The "Chase The Last Packet" button redirected to a Base64 encoded path containing Part 6.
7. **Cookies**: The redirect response set a `part7` cookie containing the final fragment.

## Tools Used
- Browser Developer Tools
- `curl`
- `base64`

## Commands
```bash
# Check headers
curl -v https://just-another-webpage--0000004.bravestone-96395b1b.southeastasia.azurecontainerapps.io/

# Check robots.txt
curl https://just-another-webpage--0000004.bravestone-96395b1b.southeastasia.azurecontainerapps.io/robots.txt
```

## Solution Methodology
1. **Systematic Enumeration**: Investigated every possible location for data storage and transmission.
2. **Fragment Collection**: Verified each fragment individually across HTML, CSS, Images, Headers, and Cookies.
3. **Reconstruction**: Assembled the 7 fragments in order to form the complete flag.

## Verified Result
- **Flag**: `bi0s{W3lc0m3_t0_th3_p4rts_0f_th3_w3bs1te_y4yy}`
- **Evidence**: Stored in `evidence/enumeration_log.txt`.
