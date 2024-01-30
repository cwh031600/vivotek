# vivotek-dos-submit

## Vulnerability type

command injection  

## Vendor of the product(s)

vivotek

## Product

vivotek
<[https://www.vivotek.com/fd8166a](https://www.vivotek.com/fd8166a)>
vivotek FD8166A

## Attack type

Remote

## Impact

Denial of Service & Rebound shell

## Affected component(s)

vivotek FD8166A

## Attack vector(s)

```python
http://192.168.1.107/cgi-bin/admin/eventtask.cgi?method=exec&file=telnetd%20-p%208999
```

## Suggested description of the vulnerability for use in the CVE

Issue found on vivotek FD8166A device. An unauthenticated attacker can use the data interface of eventtask.cgi to carefully construct a payload to complete a command injection attack. An issue was discovered on vivotek FD8166A. An unauthenticated attacker can send a request through the eventtask.cgi interface. After cgi is processed, the input is not strictly verified, resulting in imperfect filtering. Ultimately, the attacker can control the parameters of the System function to achieve unauthorized arbitrary command injection.

## Discoverer(s)/Credits

ljzjsc

## Reference(s)

[github.com](https://github.com/cwh031600/vivotek/blob/main/vivotek-FD8166A-eventtask-dos/vivotek-FD8166A-eventtask-analysis.md)

## Additional information
