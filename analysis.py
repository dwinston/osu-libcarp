with open("SAFI_results.csv") as file:
    file.readline()

    n_grass = 0
    n_mabatipitched = 0
    n_mabatisloping = 0
    ________

    for line in file:
         roof_type = line.split(",")[18] # index 18, the 19th column is C01_respondent_roof_type
         if roof_type == "grass":
             n_grass = n_grass + 1
         elif roof_type == "mabatisloping":
             n_mabatisloping += 1
         elsif _______________:
             ______________
         else:
             _____________

    print("There are", n_grass, "grass roofs")
    print("There are", n_mabatisloping, "mabatisloping roofs")
    _________
    _________
