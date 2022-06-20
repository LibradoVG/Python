Superficie_sinaloa = 57365
clima = ["calido", "subhumedo", "seco", "semiseco"]
temperatura_media_anual = "25.45"
precipitacion_anual_promedio = 790.1
Poblacion_mujeres = 1532128
Poblacion_hombres = 1494815
porcentaje_mazatlan = 16.57
porcentaje_culiacan = 33.15

#NUEVAS VARIABLES
poblacion_total = Poblacion_hombres + Poblacion_mujeres
Porcentaje_total = porcentaje_culiacan + porcentaje_mazatlan
Tercer_variable = temperatura_media_anual + " grados y los climas son: "+ clima[0] +", " +clima[1] +", "+ clima[2] +", "+ clima[3]

print(Porcentaje_total)
