# miflora2openhab
Reads sensor data from a Xiaomi Mi Flora plant sensor and provides the data to openHAB.
<br>Uses the [miflora library by open-homeautomation](https://github.com/open-homeautomation/miflora).

## Preview

````
2017-05-22 20:07:24.697314 Getting data from Mi Flora ' Lavendel '
2017-05-22 20:07:28.754408 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Firmware/state = 2.7.0
2017-05-22 20:07:29.108735 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Temperature/state = 19.6
2017-05-22 20:07:29.160244 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Moisture/state = 14
2017-05-22 20:07:29.205278 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Light/state = 2880
2017-05-22 20:07:29.306403 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Conductivity/state = 12
2017-05-22 20:07:29.354560 updated http://openhabianpi:8080/rest/items/MiFlora_Lavendel_Battery/state = 100
2017-05-22 20:07:29.357053 Finished!
2017-05-22 20:07:29.359085 Getting data from Mi Flora ' Olivenbaum '
2017-05-22 20:08:03.467706 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Firmware/state = 2.7.0
2017-05-22 20:08:03.807887 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Temperature/state = 20.2
2017-05-22 20:08:03.849746 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Moisture/state = 14
2017-05-22 20:08:03.893870 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Light/state = 4003
2017-05-22 20:08:03.938509 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Conductivity/state = 56
2017-05-22 20:08:03.986898 updated http://openhabianpi:8080/rest/items/MiFlora_Olivenbaum_Battery/state = 73
2017-05-22 20:08:03.988693 Finished!
````


## Getting Started

Clone repository `git clone https://github.com/SvenSommer/miflora2openhab`

### Prerequisites

#### Python 3
Python3 with the package `requests` is required.
````
sudo apt-get install python3
sudo apt-get install python3-requests
````

#### Get the mac address of your miflora sensor
With `bluetoothctl` you should be able to find your device
````
.../miflora2openhab$ bluetoothctl
[NEW] Controller B8:27:EB:X3:D5:77 device [default]
[NEW] Device C4:7C:8D:X2:E6:A8 Flower care
...
````

### Installing

#### Configuration of the script
Configure the script by editing the file `update2openhab.py`

Here is an example of `update2openhab.py`
```
...
openhab_host = '192.168.188.1'
openhab_port = '8080'

mac_addresses = ['C4:7C:8D:62:E6:H7','C4:7C:8D:62:E6:D8']
flower_names = ['flower1','flower2']
...
```

|Option|Description|
|---|---|
|`openhab_host`|IP address of the openhab host<br><br>**Type:** `string`<br>**Possible values:** `'192.168.188.1'`, `'localhost'`|
|`openhab_port`|Port of your openhab host<br><br>**Type:** `string`<br>**Possible values:** `'8080'` - default|
|`mac_addresses`|Mac addresses of you miflora devices<br><br>**Type:** `string-array`<br>**Possible values:** `['C4:7C:8D:62:E6:H7','C4:7C:8D:62:E6:D8']` |
|`flower_names`|Name of the flowers you would like to moinitor<br><br>**Type:** `string-array`<br>**Possible values:** `['Lavendel','Olivenbaum']` |


#### Configuration within openhab
Openhab items need to be configured within openhab. Please refer to the [documentation](http://docs.openhab.org/configuration/items.html) how to define new items.<br>
The names of the items are predefined by the names of the flowers/plants you gave in the `update2openhab.py` file.
<br>Foreach plant/floweer you need six items:
````
MiFlora_{flowername}_Firmware
MiFlora_{flowername}_Temperature
MiFlora_{flowername}_Moisture
MiFlora_{flowername}_Light
MiFlora_{flowername}_Conductivity
MiFlora_{flowername}_Battery
````

## Running the Script

The script can be started with `python3 update2openhab.py`<br><br>
I would recommend running this script within crontab
````

*/10 * * * * cd {insert_path}/miflora && python3 update2openhab.py >> {insert_path}/miflora2openhab.log

````

## Tested

This is coded and tested on a RaspberryPi 3.

## Authors

* **SvenSommer** - [SvenSommer](https://github.com/SvenSommer/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* This code is originally based on open-homeautomation project [miflora](https://github.com/open-homeautomation/miflora). Many thanks!
