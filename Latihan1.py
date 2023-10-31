def convert_to_menit(minggu, hari, jam, menit):
    return minggu * 7 * 24 * 60 + hari * 24 * 60 + jam * 60 + menit

def curried_converter(minggu):
    def step1(hari):
        def step2(jam):
            def step3(menit):
                return convert_to_menit(minggu, hari, jam, menit)
            return step3
        return step2
    return step1

data = ["3 minggu 3 hari 7 jam 21 menit",
        "5 minggu 5 hari 8 jam 11 menit",
        "7 minggu 1 hari 5 jam 33 menit"]

outputData = []

for input in data:
    bagian = input.split()
    minggu = int(bagian[0])
    hari = int(bagian[2])
    jam = int(bagian[4])
    menit = int(bagian[6])
    
    convert = curried_converter(minggu)(hari)(jam)(menit)
    outputData.append(convert)

print(outputData)
