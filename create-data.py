import json

# Datos de entrada
procesos = [
    {"nombre": "P1", "rafaga": 2, "tiempo_llegada": 0},
    {"nombre": "P2", "rafaga": 4, "tiempo_llegada": 1},
    {"nombre": "P3", "rafaga": 6, "tiempo_llegada": 2},
    {"nombre": "P4", "rafaga": 2, "tiempo_llegada": 2},
    {"nombre": "P5", "rafaga": 8, "tiempo_llegada": 3}
]

def fifo(procesos):
    procesos.sort(key=lambda x: x['tiempo_llegada'])  # Ordenar por tiempo de llegada
    tiempo_salida = []
    tiempo_final = []
    
    tiempo_actual = 0
    for proceso in procesos:
        if tiempo_actual < proceso['tiempo_llegada']:
            tiempo_actual = proceso['tiempo_llegada']
        
        tiempo_salida.append(tiempo_actual)
        tiempo_actual += proceso['rafaga']
        tiempo_final.append(tiempo_actual)
    
    return tiempo_salida, tiempo_final

def sjf(procesos):
    procesos_copia = sorted(procesos, key=lambda x: (x['tiempo_llegada'], x['rafaga']))  # Ordenar por tiempo de llegada y luego por ráfaga
    tiempo_salida = []
    tiempo_final = []
    
    tiempo_actual = 0
    procesos_restantes = procesos_copia[:]
    
    while procesos_restantes:
        lista_espera = [p for p in procesos_restantes if p['tiempo_llegada'] <= tiempo_actual]
        
        if lista_espera:
            proceso = min(lista_espera, key=lambda x: x['rafaga'])
            procesos_restantes.remove(proceso)
            
            tiempo_salida.append(tiempo_actual)
            tiempo_actual += proceso['rafaga']
            tiempo_final.append(tiempo_actual)
        else:
            tiempo_actual = min(procesos_restantes, key=lambda x: x['tiempo_llegada'])['tiempo_llegada']
    
    return tiempo_salida, tiempo_final

def prioridad(procesos):
    procesos_copia = sorted(procesos, key=lambda x: (x['tiempo_llegada'], x['rafaga']))  # Suponemos que la prioridad está implícita en el orden
    tiempo_salida = []
    tiempo_final = []
    
    tiempo_actual = 0
    procesos_restantes = procesos_copia[:]
    
    while procesos_restantes:
        lista_espera = [p for p in procesos_restantes if p['tiempo_llegada'] <= tiempo_actual]
        
        if lista_espera:
            proceso = min(lista_espera, key=lambda x: x['rafaga'])  # Suponemos que menor ráfaga implica mayor prioridad
            procesos_restantes.remove(proceso)
            
            tiempo_salida.append(tiempo_actual)
            tiempo_actual += proceso['rafaga']
            tiempo_final.append(tiempo_actual)
        else:
            tiempo_actual = min(procesos_restantes, key=lambda x: x['tiempo_llegada'])['tiempo_llegada']
    
    return tiempo_salida, tiempo_final

def crear_json():
    tiempo_salida_fifo, tiempo_final_fifo = fifo(procesos)
    tiempo_salida_sjf, tiempo_final_sjf = sjf(procesos)
    tiempo_salida_prioridad, tiempo_final_prioridad = prioridad(procesos)
    
    data = {
        "FIFO": [{"nombre": p['nombre'], "tiempo_salida": salida, "tiempo_final": final}
                 for p, salida, final in zip(procesos, tiempo_salida_fifo, tiempo_final_fifo)],
        "SJF": [{"nombre": p['nombre'], "tiempo_salida": salida, "tiempo_final": final}
                for p, salida, final in zip(procesos, tiempo_salida_sjf, tiempo_final_sjf)],
        "Prioridad": [{"nombre": p['nombre'], "tiempo_salida": salida, "tiempo_final": final}
                      for p, salida, final in zip(procesos, tiempo_salida_prioridad, tiempo_final_prioridad)]
    }
    
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)
        
    print("Archivo data.json creado con éxito.")

if __name__ == "__main__":
    crear_json()
