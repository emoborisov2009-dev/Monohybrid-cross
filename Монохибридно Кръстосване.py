q = input("Въведете наименование на алелите на индивид 1: ")
z = input("Въведете наименование на алелите на индивид 2: ")

pozvoleni_glavni_bukvi = ["А","Б","В","Г","Д","Е","Ж","З","И","Й","К","Л","М","Н","О","П","Р","С","Т","У","Ф","Х","Ц","Ч","Ш","Щ","Ъ","Ь","Ю","Я"]
pozvoleni_malki_bukvi = [i.lower() for i in pozvoleni_glavni_bukvi]
pozvoleni_bukvi = pozvoleni_glavni_bukvi + pozvoleni_malki_bukvi

if len(q) != 2 or len(z) != 2:
    print("Моля въведете по два алела за всеки индивид")

else:
    if (q[0] not in pozvoleni_bukvi or q[1] not in pozvoleni_bukvi
        or z[0] not in pozvoleni_bukvi or z[1] not in pozvoleni_bukvi):
        print("Моля запишете алелите само с български букви!")

    else:
        if q[0].upper() != q[1].upper():
            print("Моля запишете еднакви букви (Аа,аа,АА)")
        elif z[0].upper() != z[1].upper():
            print("Моля запишете еднакви букви (Аа,аа,АА)")

        else:
            if q[0].islower() and q[1].isupper():
                print("Моля запишете първо доминантния алел!")
            elif z[0].islower() and z[1].isupper():
                print("Моля запишете първо доминантния алел!")

            else:
                if q[0].upper() != z[0].upper():
                    print("Моля запишете еднакви букви и за двата индивида!")
                else:
                    if z == q and ((z[0].isupper() and z[1].isupper()) or (z[0].islower() and z[1].islower())):
                        print(f"При кръстосването на {q} и {z} в F1 получаваме {q}")
                    elif (z[0].isupper and z[1].islower) and z == q:
                        print(f"При кръстосването на {q} и {z} в F1 получаваме разпад:")
                        print(f"по фенотип – 3:1, по генотип – 1:2:1")
                        print(f"     ┃  {z[0]}   ┃  {z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[0]}  ┃  {z[0]}{q[0]}  ┃  {q[0]}{z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[1]}  ┃  {z[0]}{q[1]}  ┃  {z[1]}{q[1]}")
                    elif z[0].isupper() and z[1].isupper() and q[0].isupper() and q[1].islower():
                        print(f"При кръстосването на {q} и {z} в F1 получаваме разпад:")
                        print(f"по фенотип – 1:0, по генотип – 1:1")
                        print(f"     ┃  {z[0]}   ┃  {z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[0]}  ┃  {z[0]}{q[0]}  ┃  {q[0]}{z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[1]}  ┃  {z[0]}{q[1]}  ┃  {z[1]}{q[1]}")
                    elif z[0].isupper() and z[1].islower() and q[0].isupper() and q[1].isupper():
                        print(f"При кръстосването на {q} и {z} в F1 получаваме разпад:")
                        print(f"по фенотип – 1:0, по генотип – 1:1")
                        print(f"     ┃  {z[0]}   ┃  {z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[0]}  ┃  {q[0]}{z[0]}  ┃  {q[0]}{z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[1]}  ┃  {z[0]}{q[0]}  ┃  {q[1]}{z[1]}")
                    elif z[0].islower() and z[1].islower() and q[0].isupper() and q[1].islower():
                        print(f"При кръстосването на {q} и {z} в F1 получаваме разпад:")
                        print(f"по фенотип – 1:0, по генотип – 1:1")
                        print(f"     ┃  {z[0]}   ┃  {z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[0]}  ┃  {q[0]}{z[0]}  ┃  {q[0]}{z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[1]}  ┃  {z[0]}{q[1]}  ┃  {q[1]}{z[1]}")
                    elif z[0].isupper() and z[1].islower() and q[0].islower() and q[1].islower():
                        print(f"При кръстосването на {q} и {z} в F1 получаваме разпад:")
                        print(f"по фенотип – 1:0, по генотип – 1:1.")
                        print(f"     ┃  {z[0]}   ┃  {z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[0]}  ┃  {z[0]}{q[0]}  ┃  {q[0]}{z[1]}")
                        print("━━━━━━━━━━━━━━━━━━━")
                        print(f"  {q[1]}  ┃  {z[0]}{q[1]}  ┃  {q[1]}{z[1]}")
