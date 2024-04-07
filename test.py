tahun = range(2022, 2025)
bulan = range(1, 13)
tanggal = range(1, 32)
def tanggal_create():
    with open('tanggal.txt', 'w+') as file:
        for year in tahun:
            for month in bulan:
                if month > 9:
                    for date in tanggal:
                        if date > 9:
                            file.write(f'{year}/{month}/{date}')
                            file.write('\n')
                        else:
                            file.write(f'{year}/{month}/0{date}')
                            file.write('\n')
                else:
                    for date in tanggal:
                        if date > 9:
                            file.write(f'{year}/0{month}/{date}')
                            file.write('\n')
                        else:
                            file.write(f'{year}/0{month}/0{date}')
                            file.write('\n')
tanggal_create()