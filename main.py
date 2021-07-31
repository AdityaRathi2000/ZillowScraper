import pandas as pd
import subprocess
import house_scraper as hs


if __name__ == '__main__':
    each_house_df = pd.DataFrame(
        columns=['Asking Price', 'Bedrooms', 'Bathrooms', 'Total sqft', 'Zillow Views', 'Type', 'Year Built', 'Heating',
                 'Cooling', 'Parking', 'HOA', 'Price/Sqft', 'Sun Number'])

    links = ['https://www.zillow.com/homedetails/3900-Ford-Rd-APT-18J-Philadelphia-PA-19131/10607788_zpid/',
             'https://www.zillow.com/homedetails/3900-Ford-Rd-APT-11H-Philadelphia-PA-19131/10607684_zpid/',
             'https://www.zillow.com/homedetails/3900-Ford-Rd-APT-9L-Philadelphia-PA-19131/10607654_zpid/',
             'https://www.zillow.com/homedetails/2601-Pennsylvania-Ave-APT-513-Philadelphia-PA-19130/63498514_zpid/',
             'https://www.zillow.com/homedetails/2601-Pennsylvania-Ave-APT-134-Philadelphia-PA-19130/63498355_zpid/',
             'https://www.zillow.com/homedetails/3600-Conshohocken-Ave-APT-306-Philadelphia-PA-19131/2069344335_zpid/',
             'https://www.zillow.com/homedetails/3900-Ford-Rd-APT-5K-Philadelphia-PA-19131/10607585_zpid/',
             'https://www.zillow.com/homedetails/2601-Pennsylvania-Ave-APT-101-Philadelphia-PA-19130/63498330_zpid/']

    for each_link in links:
        a_list = hs.house_scraper(each_link)
        each_house_df.loc[len(each_house_df)] = a_list

    each_house_df["Asking Price"] = each_house_df["Asking Price"].apply(lambda x: int(x.replace(',', '').replace('$', '')))
    each_house_df["Bedrooms"] = each_house_df["Bedrooms"].apply(lambda x: int(x.replace(' bd', '').replace('--', '0')))
    each_house_df["Bathrooms"] = each_house_df["Bathrooms"].apply(lambda x: int(x.replace(' ba', '')))
    each_house_df["Total sqft"] = each_house_df["Total sqft"].apply(lambda x: int(x.replace(',', '').replace(' sqft', '')))
    each_house_df["Zillow Views"] = each_house_df["Zillow Views"].apply(lambda x: int(x.replace(',', '')))
    each_house_df["Year Built"] = each_house_df["Year Built"].apply(lambda x: int(x))
    each_house_df["Price/Sqft"] = each_house_df["Price/Sqft"].apply(lambda x: int(x.replace('$', '')))
    each_house_df["Sun Number"] = each_house_df["Sun Number"].apply(lambda x: float(x))
    each_house_df = each_house_df.drop('HOA', inplace=False, axis=1)

    writer = pd.ExcelWriter('output.xlsx')
    each_house_df.to_excel(writer)
    writer.save()
    print('Successfully exported as Excel File.')

    # Uncomment to open the file as well:
    #subprocess.check_call(['open', '-a', 'Microsoft Excel','output.xlsx'])