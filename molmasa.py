import json
import re
with open('tabula.json', 'r', encoding='utf-8') as datne:
    dati = datne.read()
dati_vardnica = json.loads(dati)
try:
    dati_vardnica = {el['symbol']: el['atomic_mass'] for el in dati_vardnica['elements']}
except (KeyError, TypeError):
    print('Kļūda JSON struktūrā, pārbaudiet savienojumu.')

def izvele(): #izskaidro noteikumus, kā arī pec tam novirza uz pareizo programmas veidu.
    print('Sveiki! Laipni lūgti molmasas aprēķināšanas programmā.')
    print('Programma darbojas 2 veidos: 1. Ātrs molmasas aprēķins. 2. Molmasas aprēķins + palīdzība, ja vēlaties beigt, tad ievadiet "b" vai "beigt".')
    try:
        while True:
            veids = input('Izvēlies programmas darbošanās veidu:')
            if veids == "1" or veids == "1.":
                atrais_aprekins()
                break
            elif veids == "2" or veids == "2.":
                molmasas_paligs()
                break
            elif veids in ["b", "beigt"]:
                print('Paldies, ka lietoji programmu! Uz redzēšanos.')
            else:
                print('Jūsu izvēle neatbilst programmas noteikumiem, ievadiet atkārtoti.')
    except SyntaxError:
        print("Jūsu izvēlētais variants neatbilst programmas variantiem.")

def atrais_aprekins(): #Programma apstrādā lietotāja ievadīto formulu un izvada tās molmasu
    while True:
        print('Jūs izvēlējāties ātro aprēķinu.')
        print('Noteikumi ir šādi:\n 1. Programma pieņem formātu: ķīmiski pareizu formulu, kā piemēram, CaCO3  \n 2. Ievadiet formulu, programma izvadīs molmasu.')
        molmasa_formula = input('Ievadiet ķīmisko formulu (vai "b", lai izietu): ').strip()
        if molmasa_formula.lower() in ["b", "beigt"]:
            print('Paldies. Lai Jums jauka diena!')
            break
        dalit = re.findall(r'([A-Z][a-z]?)(\d*)', molmasa_formula)
        if not dalit:
            print('Neatradu derīgus elementus formulā.')
            continue
        molmasa_kopa = 0.0
        for elements, skaits in dalit:
            if elements in dati_vardnica:
                masa = dati_vardnica[elements]
                daudzums = int(skaits) if skaits else 1
                molmasa_kopa += masa * daudzums
            else:
                print(f'Nezināms elements: {elements}')
                break
        else:
            print(f'Formulas {molmasa_formula} molmasa ir: {molmasa_kopa:.2f} g/mol')

def  molmasas_paligs(): #Programma apstrādā lietotāja ievadīto formulu, izvada tās molmasu un parāda kā iegūt šo rezultātu
    print("Jūs izvēlējāties aprēķinu un skaidrojumu")
    print('Noteikumi ir šādi:\n 1. Programma pieņem formātu: ķīmiski pareizu formulu, kā piemēram, CaCO3  \n 2. Ievadiet formulu, programma izvadīs molmasu.')
    while True:
        print('Jūs izvēlējāties aprēķinu un skaidrojumu.')
        molmasa_formula = input('Ievadiet ķīmisko formulu (vai "b", lai izietu): ').strip()
        if molmasa_formula.lower() in ["b", "beigt"]:
            print('Paldies. Lai Jums jauka diena!')
            break
        dalit = re.findall(r'([A-Z][a-z]?)(\d*)', molmasa_formula)
        if not dalit:
            print('Kāds no Jūsu ievadītajiem elementiem netika atrasts.')
            continue
        molmasa_kopa = 0.0
        detalas = []   #Sarakstā ievieto apstrādāto lietotāja formulu
        for elements, skaits in dalit:
            if elements in dati_vardnica:
                masa = dati_vardnica[elements]
                daudzums = int(skaits) if skaits else 1
                daļa = masa * daudzums
                detalas.append(f"{elements}: Formulā ir {daudzums} {elements} un tas ir jāreizina (*) ar:  {masa:.2f}, kas ir elementa atommasa.  {elements} iznākums formulā = {daļa:.2f}")
                molmasa_kopa += daļa
            else:
                print(f'Nezināms elements: {elements}')
                break
        else:
            print(f"\nDetalizēts sadalījums formulai {molmasa_formula}:")           
            for rinda in detalas:
                print(rinda)
            print(f"Kopējā molmasa: {molmasa_kopa:.2f} g/mol\n")


izvele()