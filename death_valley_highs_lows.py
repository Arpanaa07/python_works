filename = 'data/death_valley_2018_simple.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high = int(row[4])
            low = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

plt.title("Daily high and low temperatures - 2018\nDeath Valley, CA", fontsize=20)
