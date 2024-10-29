modal = 100_000_000
total_laba = 0

print("Modal awal: 100 juta")

for bulan in range(1, 9):
    if bulan == 1 or bulan == 2:
        laba = 0  
    elif bulan >= 3 and bulan <= 4:
        laba = modal * 0.01  
    elif bulan >= 5 and bulan <= 7:
        laba = modal * 0.05 
    else:
        laba = modal * 0.03  

    total_laba += laba
    print(f"laba bulan ke-{bulan} sebesar: {int(laba)}")

print(f"Total laba adalah: {int(total_laba)}")
