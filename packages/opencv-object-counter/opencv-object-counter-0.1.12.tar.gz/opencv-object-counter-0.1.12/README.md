# OpenCV2 Object Counter
Count objects using opencv2 in this configurable CLI utility. The module uses frame differencing to detect and count objects according to a flexible configuration scheme. This makes it a quick-and-dirty solution that can achieve good accuracy in a variety of cases and doesn't involve the computaional overhead nor complexity of convolutional neural netowrks (CNN). 

Alternatively, the package can be imported to your own scripts.

## Gates
`Gates` are the instrument used for counting. They are boxes which detect  objects passing through them. A cooldown is triggered when it detects an object to avoid counting the same object many times. The right cooldown duration will depend on the counting situation. An object is counted if the gate is not on cooldown and the center point of the object and the gate is within the given distance.

## Configuration
Here is an annotated example config. A default config is provided in `ooc/config.json`. Running `ooc` in cli mode requires a config. More details on some of the parameters can be found on `https://docs.opencv.org/`.

*Note: The comments provided in this snippet are for informational purposes only and render this invalid JSON.*

```js
{
    // list of gates that will be used for counting
    "gates": [
        {
            // Starting x and y position (0,0 is top left)
            // and gate dimnensions
            "x": 350,
            "y": 320,
            "width": 100,
            "height": 100
        }
    ],
    "blur" : {
        // openCV2 kernal size
        // must be positive or odd, or 0 (in which case 
        // they are computed from sigma)
        "ksize": {
            "width": 21,
            "height": 21
        },
        // openCV2 kernal standard deviation
        "sigma_x": 0
    },
    // whether or not the video shows. press 'q' to quit
    "show": true,
    // whether or not additional video shows/logs print
    "debug": false
}
```

## Command Line Arguments

-s, --source 
 - required
 - Path to the video to analyze.
 - Usage: `ooc -s /path/to/video.mp4`

-t, --show
 - Displays the video if set.

-d, --debug
 - Runs in debug mode, which includes visual on the video (if -s is set) and prints logs.

-c, --config
- Path to config file. If not set, the default config is 
used.
- Usage: `ooc -s /path/to/video.mp4 -c /path/to/config.json`

## Example Run

```
python ooc/cli.py -s /path/to/video.mp4 -c /path/to/config.json
```