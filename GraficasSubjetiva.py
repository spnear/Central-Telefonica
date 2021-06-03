import matplotlib.pyplot as plt
treinta = [3.43,2.75,2.63,2.6,2.1]
veinte = [2.75,2.687,2.525,2.125,1.3125]
porcentaje = ["1%","2%","3%","4%","5%",]
plt.figure(1)
plt.bar(porcentaje,treinta,color='red',alpha=0.8)
plt.xlabel("Patrón de pérdidas")
plt.ylabel("MOS")
plt.title("Calificación Subjetiva MOS vs Patrón de pérdidas")
plt.bar(porcentaje,veinte,color='blue',alpha=0.5)
plt.legend(["30ms","20ms"])
plt.grid()

objveinte = [2.72,2.57,2.41,2.12,1.88]
objtreinta = [2.71,2.68,2.65,2.61,2.59]
porc = [1,2,3,4,5]

plt.figure(2)
plt.subplot(1,2,1)
plt.grid()
plt.plot(porc,objveinte)
plt.plot(porc,veinte)
plt.title("Calificación Objetiva y Subjetiva,Longitud 20mS")
plt.legend(["Objetiva","Subjetiva"])

plt.subplot(1,2,2)
plt.grid()
plt.plot(porc,objtreinta)
plt.plot(porc,treinta)
plt.title("Calificación Objetiva y Subjetiva,Longitud 30mS")
plt.legend(["Objetiva","Subjetiva"])
plt.show()