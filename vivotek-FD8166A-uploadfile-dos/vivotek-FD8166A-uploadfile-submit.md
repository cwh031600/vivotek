# Tplink-wr886n-v6-cloud_config-device_legality_illegal-dos-submit

## Vulnerability type

command injection  

## Vendor of the product(s)

vivotek

## Product

vivotek <https://www.vivotek.com/fd8166a> vivotek FD8166A

## Attack type

Remote

## Impact

Denial of Service

## Affected component(s)

vivotek FD8166A

## Attack vector(s)

```python
http://192.168.1.107/cgi-bin/admin/update_lens.cgi?choose_lens=2;id;34
```

## Suggested description of the vulnerability for use in the CVE

Issue found on vivotek FD8166A device. An unauthenticated attacker can use the data interface of upload_file.cgi to carefully construct a payload to complete a command injection attack. An issue was discovered on vivotek FD8166A. An unauthenticated attacker can send a request through the upload_file.cgi interface. After cgi is processed, the input is not strictly verified, resulting in imperfect filtering. Ultimately, the attacker can control the parameters of the System function to achieve unauthorized arbitrary command injection.

## Discoverer(s)/Credits

ljzjsc

## Reference(s)

github.com

## Additional information
