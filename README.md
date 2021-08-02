# Last 14 Days Highs/Lows script for WeatherCat

This is a Python script that will automatically generate an image file from a set of
[WeatherCat](https://trixology.com) weather station data.

Set it up to run every few minutes or hours and output into a web server and reference
it from wherever you want. I insert it in my [local weather station page](https://snell.zone/weather/weather.php).

![latesttemps](https://user-images.githubusercontent.com/3698050/127919442-70fa98d7-a199-4f4c-bd9b-c7051dffc55b.png)

Requires python 3 and uses modules matplotlib and datetime.

You'll need to set the paths to your WeatherCat data file (usually /Users/_your-username_/Library/WeatherCatData/_your-locationname_/) 
and where you'd like to save the output file.

I also added an option to use Celsius for metric types.

Feel free to use, modify, and submit additions. I'd love to hear if you decide to use this.

-Jason Snell, jsnell@sixcolors.com
