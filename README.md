# Script voor het reformatten van NLB notebalk afbeeldingen

De [nieuwe liedboek (NLB, https://liedboek.liedbundels.nu/)](https://liedboek.liedbundels.nu/) wordt op de website te download aangeboden als
afbeeldingen met notebalken. Helaas hebben deze niet niet full-HD formaat die
voor veel beamers gebruikt worden. Om het importeren van de afbeeldingen in
presentatie programma's (Zoals PowerPoint en EasyWorship) makker te maken,
is een python programma gemaakt die de gedownloade afbeeldingen inleest en
reformat naar een 1920x1080px afbeelding. Daarnaast wordt er een titel aan de
afbeelding toegevoegd.


## Titel in de afbeeldingen
Links bovenin wordt een titel toegevoegd om het desbetreffende nummer en couplet
aan te geven.\
Gebruikte formaat: NLB {liednummer} : {couplet nummer}.\
Bij refrein wordt het couplet nummer vervangen door refrein. Daarnaast wordt een
vreemde taal (alles buiten nederlands) aangegeven met haakjes.

**Voorbeelden:**\
NLB 10 : 1\
NLB 10 : refrein\
NLB 10 : 1 (en)
\

## requirements

Het programma is gemaakt met Python 3.7

De volgende packages moeten geinstalleerd zijn:
* NumPy ([v1.17.2](https://github.com/numpy/numpy/releases); [BSD License](https://www.numpy.org/license.html))  
* Pillow ([6.2.0](https://github.com/python-pillow/Pillow/releases); [open source PIL Software License](https://github.com/python-pillow/Pillow/blob/master/LICENSE))

Installatie van de packages met python package manager (pip):
```  
pip install -r requirements.txt
```  


## Font
Voor het maken van de titels is een font file vereist (ttf file). Het Verdana
fot kan gemakkelijk gedownload worden via:
[https://www.fontpalace.com/font-download/Verdana+Bold/](https://www.fontpalace.com/font-download/Verdana+Bold/)

## Gebruik van programma
Het programma heeft een path nodig naar de map waar de png afbeeldingen staan
afkomstig van de NLB website en de path naar de font (ttf) file
```  
nlb-notenbalk-afbeelding-formatter.py -i "path/to/image/dir/" -f "path/to/font/file"
```  

## Authors  
Henry Wiersma

## License
This project is licensed under the GNU GPL v3 license - see the [LICENSE.md](LICENSE.md) file for details.
