import pandas as pd

#Scrape forwards' data
ending_year = [17, 18]

columns = ['Player', 'TOI/GP', 'Goals/60', 'Total Assists/60', 'IPP', 'Shots/60', 'SH%', 'ixG/60', 'iCF/60', 'iSCF/60', 'iHDCF/60', 'Hits/60', 'Shots Blocked/60']

while ending_year[1] < 24:
    year = f'20{ending_year[0]}20{ending_year[1]}'
    url = f'https://www.naturalstattrick.com/playerteams.php?fromseason={year}&thruseason={year}&stype=2&sit=all&score=all&stdoi=std&rate=y&team=ALL&pos=F&loc=B&toi=600&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL'

    df = pd.read_html(url)
    df = df[0]
    df = df.loc[:,columns]

    df.to_csv(f'forwards20{ending_year[1]}.csv', index=False)

    ending_year[0] += 1
    ending_year[1] += 1



#Scrape Defenseman data
ending_year = [17, 18]

while ending_year[1] < 24:
    year = f'20{ending_year[0]}20{ending_year[1]}'
    url = f'https://www.naturalstattrick.com/playerteams.php?fromseason={year}&thruseason={year}&stype=2&sit=all&score=all&stdoi=std&rate=y&team=ALL&pos=D&loc=B&toi=600&gpfilt=none&fd=&td=&tgp=410&lines=single&draftteam=ALL'

    df = pd.read_html(url)
    df = df[0]
    df = df.loc[:,columns]

    df.to_csv(f'defenseman20{ending_year[1]}.csv', index=False)

    ending_year[0] += 1
    ending_year[1] += 1