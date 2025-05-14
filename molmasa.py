import json
import re
with open('tabula.json', 'r', encoding='utf-8') as datne:
    dati = datne.read()
dati_vardnica = json.loads(dati)
try:
    dati_vardnica = {el['symbol']: el['atomic_mass'] for el in dati_vardnica['elements']}
except (KeyError, TypeError):
    print('Kļūda JSON struktūrā')

def izvele():
    print('Sveiki! Laipni lūgti molmasas aprēķināšanas programmā.')
    print('Programma darbojas 2 veidos: 1. Ātrs molmasas aprēķins. 2. Molmasas aprēķins + palīdzība, ja vēlaties beigt, tad ievadiet "b" vai "beigt".')
    try:
        molmasa = True
        while molmasa == True:
            veids = input('Izvēlies programmas darbošanās veidu: 1 vai 2')
            if veids == "1" or veids == "1.":
                atrais_aprekins()
                break
            elif veids == "2" or veids == "2.":
                molmasas_paligs()
                break
            elif veids == "b" or veids == "beigt":
                molmasa = False
            else:
                print('Jūsu izvēle neatbilst programmas noteikumiem, ievadiet atkārtoti.')
    except SyntaxError:
        print("Jūsu izvēlētais variants neatbilst programmas variantiem.")

def atrais_aprekins():
    print('Jūs izvēlējāties ātro aprēķinu')
    print('Noteikumi ir šādi:\n 1. Programma pieņem formātu: ķīmiski pareizu formulu, kā piemēram, CaCO3  \n 2. Ievadiet formulu, programma izvadīs molmasu.')
    molmasa_formula = input('Ievadiet ķīmisko formulu: ').strip()
    dalit = re.findall(r'([A-Z][a-z]?)(\d*)', molmasa_formula)
    if not dalit:
        print('Neatradu derīgus elementus formulā.')
        return
    molmasa_kopa = 0.0
    for elements, skaits in dalit:
        if elements in dati_vardnica:
            masa = dati_vardnica[elements]
            daudzums = int(skaits) if skaits != '' else 1
            molmasa_kopa += masa * daudzums
        else:
            print(f'Nezināms elements: {elements}')
            return

    print(f'Formulas {molmasa_formula} molmasa ir: {molmasa_kopa:.2f} g/mol')

def  molmasas_paligs():
    print("Jūs izvēlējāties aprēķinu un skaidrojumu")
    print('Noteikumi ir šādi:\n 1. Programma pieņem formātu: ķīmiski pareizu formulu, kā piemēram, CaCO3  \n 2. Ievadiet formulu, programma izvadīs molmasu.')
    molmasa_formula = input('Ievadiet ķīmisko formulu: ').strip()
    dalit = re.findall(r'([A-Z][a-z]?)(\d*)', molmasa_formula)
    if not dalit:
        print('Neatradu derīgus elementus formulā.')
        return
    molmasa_kopa = 0.0
    for elements, skaits in dalit:
        if elements in dati_vardnica:
            masa = dati_vardnica[elements]
            daudzums = int(skaits) if skaits != '' else 1
            molmasa_kopa += masa * daudzums
        else:
            print(f'Nezināms elements: {elements}')
            return
    print(f'Formulas {molmasa_formula} molmasa ir:  {molmasa_kopa:.2f} g/mol, jo {dalit} elementu atommasas ir {masa} un {daudzums}')


izvele()