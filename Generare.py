

""" import os

for i in range(1, 64):
    os.mkdir('4CB19CS0' + str(i)) """




""" import bs4 as bs
import re 

bs = bs.BeautifulSoup(open('z.html'), 'lxml') """



l = ['ABHISHEK D DEVADIGA', 'ADITHYA PAI B', 'ADITI K A', 'ADITYA S BHANDARY', 'AINISHA RODRIGUES', 'AISHWARYA PRAKASH', 'AJAYKRISHNA M', 'AKARSH T', 'AKARSHITHA P KINI', 'AKSHAY P BHANDARKAR', 'AMOGH N BANARE', 'AMRUTHA A SHANBHAG', 'ANIKETH B R', 'ANIRUDDHA', 'ANKITA VASANT NAIK', 'ANKITH T', 'ANMOL R KAMATH', 'ANVITHA K R', 'APEKSHA SHETTY', 'ASHLESHA PRAMOD PAI', 'ASHWINI PAI', 'ATHMIK ASHOK HEGDE K', 'B ANJANA SHENOY', 'B APOORVA NAYAK', 'B ASHWITHA NAYAK', 'BABITH', 'BHOOMIKA', 'BHOOMIKA VISHNU NAIK', 'CHANDRAHAS PAI', 'CHARISHMA', 'CHETHAN KRISHNA', 'DAMODARA HEGDE KL', 'DHANASHREE BHAT', 'DHANUSH S A', 'DHRUVA D NAYAK', 'DISHA S SHENOY', 'DIYA', 'ELVIN MARCIAN DOMINIC DSOUZA', 'GAGAN NIRANJAN NAIK', 'GAUTHAM ALVA', 'GG ASHWIN PRABHU', 'HARSHITHA', 'HARSHITHA R ULLALBAIL', 'ISMAIL IHTHISHAM', 'JATIN PANDIT', 'K KESHAVA BHAT', 'KARTHIK B', 'KARTHIK M K', 'KARTHIK M KASHYAP', 'KREETHAN DSOUZA', 'KRUTHIKA CS', 'LEKHANA B Y', 'M ANMOL KAMATH', 'M ANUSHKA BHAT', 'M PRAJWAL KINI', 'MAITHRI V HOLLA', 'MEGHNA', 'MELWIN NELSON PINTO', 'MUKUND P PAI', 'N PRATEEKA PAI', 'NANDISH SHENOY P H', 'NAYANA VINAYAK GUNDU', 'NITHINKUMAR U']

""" print the name and index +1  """

""" for i in range(len(l)):
    print(i+1, l[i])
 """




for i in range(len(l)):
    with open('4CB19CS00' + str(i+1) + '/README.md', 'w') as f:
        f.write('# ' + l[i] + '\n' + '## USN :'  + '4CB19CS0' + str(i+1) )
