lon = float(input())
lat = float(input())
DH = ((lon - 34)**2 + (lat - 220)**2)**(1/2)
DK = ((lon - 0)**2 + (lat - 0)**2)**(1/2)
DS = ((lon - 140)**2 + (lat - 456)**2)**(1/2)
DH = round(DH, 2)
DK = round(DK, 2)
DS = round(DS, 2)
print('Distancia para Hogsmeade:',f'{DH:.2f}')
print('Distancia para Kakariko:',f'{DK:.2f}')
print('Distancia para Solitude:',f'{DS:.2f}')