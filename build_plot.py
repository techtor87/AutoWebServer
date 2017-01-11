import matplotlib.pyplot as plt
import matplotlib.dates as mdate


def cust_burndown_plot(title_str, xdates: list, ydata:list, output_file_str = ''):
    weeks = mdate.WeekdayLocator()
    days  = mdate.DayLocator()
    if not isinstance(xdates, list):
        raise TypeError
    if not isinstance(ydata, list):
        raise TypeError

    fig, ax = plt.subplots()
    plt.title(title_str)

    for line in ydata:
        if not isinstance(line, list):
            raise TypeError

        ax.plot(xdates, line[0], label=line[1])

    ax.xaxis.set_major_locator(weeks)
    ax.xaxis.set_major_formatter(mdate.DateFormatter('%m/%d'))
    ax.xaxis.set_minor_locator(days)
    ax.yaxis.grid(color='gray')
    #ax.set_xlim(xdates[0][0], xdates[0][len(xdates)-1])
    ax.format_xdata = mdate.DateFormatter('%m-%d')
    fig.autofmt_xdate()
    legend = plt.legend()

    if output_file_str != '':
        plt.savefig(output_file_str, bbox_inches='tight')
    else:
        plt.show()

    plt.close()

    return
