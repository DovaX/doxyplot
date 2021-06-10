# Doxyplot

Doxyplot is a plotting wrapper around matplotlib for easy plotting.

## Installation

(Not ready yet)
Use the package manager [pip](https://pip.pypa.io/en/stable/) to install Doxyplot.

```
pip install doxyplot
```

## Usage


```
import doxyplot.doxyplot_core as dp

plot = dp.Doxyplot()

x=[1,2,3,4]
y=[4,5,4.5,2]
y2=[5,7,2,1]
y3=[10,9,5,4]
y4=[5,4,2,2]

plot.append_data(x, y, 'r', 'Line1', linewidth=2.0)
plot.append_data(x, y2, 'k', 'Line2', linewidth=2.0)
plot.append_data(x,y3, c='g', label='Line3')
plot.append_data(x,y4, c='b', label='Line4')
plot.construct_plot("Doxyplot", "Time", "Velocity",save="export.png")
```


![alt text](https://github.com/DovaX/doxyplot/blob/master/export.png?raw=true)


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
