# Rhubarb -> Tapir Lab. dönüşüm haritası
rhubarb_to_tapir = {
       "A": 2,  # AI -> i -> 2
       "D": 2,  # AI -> i -> 2
       "C": 1,  # E -> e -> 1
       "E": 3,  # O -> o -> 3 +
       "F": 4,  # U -> u -> 4 +
       "X": 0,  # rest -> 0 (a) veya boş bırakılabilir
    # in report a-> 0, e -> 1, i -> 2, o -> 3, u -> 4
    
    #"D": 0,
    #"C": 1,
    #"A": 2,
    #"E": 3,
    #"F": 4,
    #"X": 20
}


def convert_output_to_tapir(input_file, output_file):
    # output.txt dosyasını oku
    with open(input_file, 'r') as file:
        lines = file.readlines()
    
    converted_data = []
    
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) == 2:
            time_stamp, rhubarb_shape = parts
            tapir_shape = rhubarb_to_tapir.get(rhubarb_shape, 0)  # Harita yoksa rest (0) ata
            converted_data.append(f"{time_stamp}\t{tapir_shape}")
    
    # Yeni dönüştürülmüş dosyayı kaydet
    with open(output_file, 'w') as file:
        file.write("\n".join(converted_data))

# Kullanım

convert_output_to_tapir("/Users/seherova/Documents/projectss/Rhubarb-Lip-Sync/output.txt", "/Users/seherova/Documents/projectss/Rhubarb-Lip-Sync/converted_output.txt")
print("Dönüştürme tamamlandı! converted_output.txt oluşturuldu.")
