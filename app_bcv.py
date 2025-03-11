import bcv_now
import bcv_date
import download_file

class TasaBCV():
    def __init__(self):
        pass
    
    def hoy():
        """Retorna un String con la Tasa del bcv de la fecha actual"""
        return bcv_now.ExtraerTasaBCV().hoy()
    
    def fecha(fecha_entrada):
        """Entrada de fecha en str (DD/MM/AAA)"""
        bcv_fecha = bcv_date.ExtraerBCVFecha(fecha_entrada)
        gestion = download_file.Gestion_data()
        

        
        if bcv_fecha.es_hoy():
            return bcv_now.ExtraerTasaBCV().hoy()
        else:
            if bcv_fecha.fecha_existe():
                return bcv_fecha.fecha_existe()
            else:
                try:
                    bcv_fecha.tasaBCV()
                    return bcv_fecha.tasaBCV()                   
                except:
                    try:
                        gestion.descargar_archivo()
                    except:
                        print(f'error al actualizar la data, se tiene registro hasta: {bcv_fecha.ultimo_registro()}')
                try: 
                    bcv_fecha.tasaBCV()
                    return bcv_fecha.tasaBCV()
                        
                except:
                    if bcv_fecha.tres_dias():
                        return bcv_now.ExtraerTasaBCV().hoy()
                    return 'No se encontro la fecha en la data, intenta con otra'
        
    def desde_hasta(fecha_inicio, fecha_fin):
        """devuelve un diccionario con un rango de tasas 'DD/MM/AA' : 'xx.xxx'"""
        from datetime import datetime, timedelta

        fecha_inicio_dt = datetime.strptime(fecha_inicio, "%d/%m/%Y")
        fecha_fin_dt = datetime.strptime(fecha_fin, "%d/%m/%Y")

        tasas = {}

        fecha_actual = fecha_inicio_dt
        while fecha_actual <= fecha_fin_dt:
            bcv_fecha = bcv_date.ExtraerBCVFecha(fecha_actual.strftime("%d/%m/%Y"))
            tasa = bcv_fecha.tasaBCV()
            tasas[fecha_actual.strftime("%d/%m/%Y")] = tasa

            # para ir avanzando en en el rango
            fecha_actual += timedelta(days=1)

        return tasas
        
tasaBCV = TasaBCV()

# print(TasaBCV.hoy())
# print(TasaBCV.fecha('31/1/2025'))
# print(TasaBCV.desde_hasta('10/2/2025', '20/2/2025'))