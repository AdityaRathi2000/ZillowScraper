import pandas as pd
import subprocess
import house_scraper as hs
import time

if __name__ == '__main__':

    uniquezips = ['19120', '19140', '19133', '19134', '19132', '19124', '19131', '19142', '19144', '19143'] #

    all_dfs = []
    for i in uniquezips:
        ebig = list(hs.link_scraper('https://www.zillow.com/philadelphia-pa-{}'.format(i)))
        for esmall in range(len(ebig)):
            df_created = hs.house_scraper(i, ebig[esmall])
            all_dfs.append(df_created)
        print("~~~~~~just wrapped up zip: {}~~~~~~".format(i))

    result = pd.concat(all_dfs).reset_index(drop=True)
    print(result)

    writer = pd.ExcelWriter('output.xlsx')
    result.to_excel(writer)
    writer.save()
    print('Successfully exported as Excel File.')

    # Uncomment to open the file as well:
    #subprocess.check_call(['open', '-a', 'Microsoft Excel','output.xlsx'])
