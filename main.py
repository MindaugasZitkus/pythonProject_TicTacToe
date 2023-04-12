# Tic-Tac-Toe zaidimas  Python'e.

pavyzdine_lenta = '|1|2|3|\n|4|5|6|\n|7|8|9|'
print('Tic-Tac-Toe Žaidimas (pavyzdinė lenta,loginis skaičių pozicijų išdėstymas lentoje): \n' + pavyzdine_lenta)
print('----------------------------------------------------------')
print("Žaidimo pradžia  --  Žaidėjas 1  [X]  --  Žaidėjas 2 [O]\n")

# Kiekvienas raktas zodyne/sarase reiskia pozicija lentoje, o raktai yra poziciju numeriai
# Po kiekvieno zaidejo pasirinkto ejimo verte/raktas bus irasytas ir vietoj tuscio rodys X arba 0

lenta = {'1': ' ', '2': ' ', '3': ' ',
         '4': ' ', '5': ' ', '6': ' ',
         '7': ' ', '8': ' ', '9': ' '}

lentos_raktas = []

for raktas in lenta:
    lentos_raktas.append(raktas)  # .append prides zaidejo pasirinkima(rakta') vietoj tuscio langelio prisides X arba 0


#  Funkcija spausdina lenta
def spausdinti_lenta(lenta):
    print(' ' + lenta['1'] + ' | ' + lenta['2'] + ' | ' + lenta['3'] + ' ')
    print('---+---+---')
    print(' ' + lenta['4'] + ' | ' + lenta['5'] + ' | ' + lenta['6'] + ' ')
    print('---+---+---')
    print(' ' + lenta['7'] + ' | ' + lenta['8'] + ' | ' + lenta['9'] + ' ')


# Pagrindine zaidimo funkcija
def zaidimas():
    eile = 'X'  #X visalaik pradeda pirmas
    skaiciuoti = 0

    # zaidimo ciklas spausdins vis atnaujinta lenta rodo maksimalu iteracijos apsisukimo veikima
    for i in range(10):
        spausdinti_lenta(lenta)
        print("Tavo eilė," + eile + ".Įveskite pozicijos skaicių tarp  [1-9] ten kur norite pažymėti? ")

        ejimas = input()

        if lenta[ejimas] == ' ':
            lenta[ejimas] = eile
            skaiciuoti += 1
        else:
            print("Šis langelis jau užimtas.\nPasirinkite kita vieta?")
            continue

        # Patikrinsim ar zaidejas X ar 0 laimejo,su if elif funkcija patikrinam visus galimus vertikaliu, horizontaliu, bei istrizu langeliu laimejimu variantus
        if skaiciuoti >= 5:
            if lenta['1'] == lenta['2'] == lenta['3'] != ' ':   # horizontaliai virsutine eilute
                spausdinti_lenta(lenta)                         # X| X | X == Jei 1 lygus 2 ir jei 2 lygus 3 == Laimejai (Ivestas)  'X arba 0'
                print("Žaidimo pabaiga.")                       # 4| 5 | 6
                print("---- " + eile + " Laimėjai ---- ")       # 7| 8 | 9
                break                                           #break = iskart sustabdom zaidima jei turime laimetoja
            elif lenta['4'] == lenta['5'] == lenta['6'] != ' ':  # horizontaliai per viduri
                spausdinti_lenta(lenta)
                print("Žaidimo pabaiga.")
                print("---- " + eile + " Laimėjai ---- ")
                break
            elif lenta['7'] == lenta['8'] == lenta['9'] != ' ':  # horizontaliai per apacia
                spausdinti_lenta(lenta)
                print("Žaidimo pabaiga.")
                print("---- " + eile + " Laimėjai ---- ")
                break
            elif lenta['1'] == lenta['4'] == lenta['7'] != ' ':  # vertikaliai
                spausdinti_lenta(lenta)
                print("Žaidimo pabaiga.")
                print("---- " + eile + " Laimėjai ---- ")
                break
            elif lenta['2'] == lenta['5'] == lenta['8'] != ' ':  # vertikaliai per viduri
                spausdinti_lenta(lenta)                          # 1 | X | 3
                print("Žaidimo pabaiga.")                        # 4 | X | 6
                print("---- " + eile + " Laimėjai ---- ")        # 7 | X | 9    3 X == Laimejai
                break
            elif lenta['3'] == lenta['6'] == lenta['9'] != ' ':  # vertikaliai
                spausdinti_lenta(lenta)
                print("Žaidimo pabaiga.")
                print("---- " + eile + " Laimėjai ---- ")
                break
            elif lenta['3'] == lenta['5'] == lenta['7'] != ' ':  # isrizai
                spausdinti_lenta(lenta)
                print("Žaidimo pabaiga.")
                print("---- " + eile + " Laimėjai ---- ")
                break
            elif lenta['1'] == lenta['5'] == lenta['9'] != ' ':  # istrizai
                spausdinti_lenta(lenta)                          # X | 2 | 3
                print("Žaidimo pabaiga.")                        # 4 | X | 6
                print("---- " + eile + " Laimėjai ---- ")        # 7 | 8 | X istrizaine 3 X == Laimejai
                break

                # Po 9 ejimo jei lenta yra pilna ir nei vienas nelaimejo skelbiama lygiosios
        if skaiciuoti == 9:
            print("Žaidimo pabaiga.")
            print("Lygiosios!")

        # Pakeiciam zaidejus po kiekvieno ejimo
        if eile == 'X':
            eile = 'O'
        else:
            eile = 'X'

            # . Leidzia zaisti is naujo
    is_naujo = input("Ar norite žaisti dar karta?(t/n)")
    if is_naujo == "t":  # is_naujo lygus t raidei paspaudus t raide leis zaist is naujo
        for raktas in lentos_raktas:  # vel iteruojam per lentos_rakta
            lenta[raktas] = " "
        zaidimas()
    else:
        print('Žaidimo pabaiga')


if __name__ == "__main__":
    zaidimas()
