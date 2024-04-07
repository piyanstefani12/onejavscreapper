tahun = range(2022, 2025)
bulan = range(1, 13)
tanggal = range(1, 32)

for year in tahun:
    for month in bulan:
        if month > 9:
            for date in tanggal:
                if date > 9:
                    print(f'{year}/{month}/{date}')
                else:
                    print(f'{year}/{month}/0{date}')
        else:
            for date in tanggal:
                if date > 9:
                    print(f'{year}/0{month}/{date}')
                else:
                    print(f'{year}/0{month}/0{date}')


