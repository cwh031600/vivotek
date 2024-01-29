# Tplink-wr886n-v6-cloud_config-device_legality_illegal-dos-submit

## Vulnerability type

command injection  

## Vendor of the product(s)

vivotek

## Product

tp-link-450M  
<https://www.tp-link.com.cn/product_733.html>
TP-Link TL-WR886N 6.0 2.2.6

## Attack type

Remote

## Impact

Denial of Service & Rebound shell

## Affected component(s)

TP-Link TL-WR886N 6.0 2.2.6

## Attack vector(s)

```python
http://192.168.1.107/cgi-bin/admin/eventtask.cgi?method=exec&file=telnetd%20-p%208999
```

## Suggested description of the vulnerability for use in the CVE

Issue found on vivotek FD8166A device. An unauthenticated attacker can use the data interface of eventtask.cgi to carefully construct a payload to complete a command injection attack. An issue was discovered on vivotek FD8166A. An unauthenticated attacker can send a request through the eventtask.cgi interface. After cgi is processed, the input is not strictly verified, resulting in imperfect filtering. Ultimately, the attacker can control the parameters of the System function to achieve unauthorized arbitrary command injection.

## Discoverer(s)/Credits

ljzjsc

## Reference(s)

github.com

## Additional information
