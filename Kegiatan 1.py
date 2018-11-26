D = {1 : 'Muhammad Irfan', 2 : 'L200184165', 3 : 'Tangerang', 4 : '13175', 5 : 'laki laki', 6 : '13 jul 2000', 7 : 'Universitas Muhammadiyah Surakarta'}



def data1(nama):

    "Displaying Name "

    print( nama, D[1] )

    return;

def data2(nim):

    "Displaying NIM "

    print( nim, D[2] )

    return;

def data3(alamat):

    "Displaying Addres "

    print( alamat, D[3] )
    return;

def data4(kodepos):

    "Displaying postal code "

    print( kodepos, D[4] )

    return;

def data5(jenis):

    "Displaying Gender "

    print( jenis, D[5] )

    return;

def data6(lahir):

    "Displaying day of birth "

    print( lahir, D[6] )

    return;

def data7(univ):

    "Displaying your university name "

    print( univ, D[7] )

    return;

def data8(awal, belakang):

    "Displaying Option "

    print( awal, 'Displaying', belakang )

    return;



x = "s"

while x != "k" :

    print ("You can see your personal identity here")

    print ("Please choose, Press b for help")

    x = str(input("Enter Your option : "))

    if x == "b":

        print ("The Option : ")

        data8("b   ", "Help ")

        data8("n   ", "name ")

        data8("N   ", "NIM ")

        data8("A   ", "addres ")

        data8("K   ", "postal code ")

        data8("J   ", "gender ")

        data8("T   ", "Date of Birth ")

        data8("U   ", "University Name")

        data8("k   ", "Exit ")

        

    elif x == "n":

        data1('Your name is ');

    elif x == "N":

        data2('Your NIM is ');

    elif x == "A":

        data3('Your addres is ');

    elif x == "K":

        data4('Your postal code is ');

    elif x == "J":

        data5('Your gender is ');

    elif x == "T":

        data6('Your Date of birth is ');

    elif x == "U":

        data7('Your University Name is ');
