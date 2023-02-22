def header(label,data):

    row = "{0:^5} | ".format(label)
    
    while data <= 60:

        strData = "{0}".format(data)

        rowWindspeed = " {0:^4s} ".format(str(strData))

        row = row + str(rowWindspeed)

        data = data + 5
    return row

def row(label,data):

    row = "{0:^5} | ".format(label)
    
    while data <= 60:

        strData = "{0}".format(windchill(data,label))

        rowWindspeed = " {0:^4s} ".format(str(strData))

        row = row + str(rowWindspeed)

        data = data + 5
    return row

def windchill(T,V):

    windchill = int(35.74 + (0.6212 * T) - (35.75 * (V ** 0.16)) \
     + (0.4275 * T * (V ** .016)))

    return windchill

def main():

    T,V = -20,5

    #print("{0:^5}{1:^10}{2:^5}".format("Wind\nSpeed", T, T+10))

    print(header("Wind\nSpeed", T))

    while V <= 50:

        print(row(V,T))

        V = V + 5

    print(windchill(-20,50))

main()