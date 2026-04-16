"""
mi_agente.py — Aquí defines tu agente.
╔══════════════════════════════════════════════╗
║  ✏️  EDITA ESTE ARCHIVO                      ║
╚══════════════════════════════════════════════╝

Tu agente debe:
    1. Heredar de la clase Agente
    2. Implementar el método decidir(percepcion)
    3. Retornar: 'arriba', 'abajo', 'izquierda' o 'derecha'

Lo que recibes en 'percepcion':
───────────────────────────────
percepcion = {
    'posicion':       (3, 5),          # Tu fila y columna actual
    'arriba':         'libre',         # Qué hay arriba
    'abajo':          'pared',         # Qué hay abajo
    'izquierda':      'libre',         # Qué hay a la izquierda
    'derecha':        None,            # None = fuera del mapa

    # OPCIONAL — brújula hacia la meta.
    # No es percepción real del entorno, es información global.
    # Usarla hace el ejercicio más fácil. No usarla es más realista.
    'direccion_meta': ('abajo', 'derecha'),
}

Valores posibles de cada dirección:
    'libre'  → puedes moverte ahí
    'pared'  → bloqueado
    'meta'   → ¡la meta! ve hacia allá
    None     → borde del mapa, no puedes ir

Si tu agente retorna un movimiento inválido (hacia pared o
fuera del mapa), simplemente se queda en su lugar.
"""

from entorno import Agente


class MiAgente(Agente):
    """
    Tu agente de navegación.

    Implementa el método decidir() para que el agente
    llegue del punto A al punto B en el grid.
    """

    def __init__(self):
        super().__init__(nombre="Mi Agente")
        # Estado interno (memoria): un diccionario para contar cuántas veces hemos visitado cada celda
        self.conteo_visitas = {}

    def al_iniciar(self):
        """Se llama una vez al iniciar la simulación. Opcional."""
        pass
        # Inicializamos el conteo de visitas aquí para asegurarnos de que se reinicie cada vez que se ejecute la simulación.
        self.conteo_visitas = {}

    def calcular_utilidad(self, accion, percepcion, pos_actual):
        """
        El núcleo del agente. Calcula qué tan 'útil' es dar un paso en cierta dirección.
        """
        # 1. Utilidad Base: Cada paso tiene un costo de -1. 
        # Esto obliga al agente a buscar la ruta más corta (menos pasos).
        utilidad = -1

        celda_destino = percepcion[accion]

        # 2. Evaluación de obstáculos (Peligro mortal)
        if celda_destino == 'pared' or celda_destino is None:
            return -1000  # Castigo máximo, nunca elegirá esto

        # 3. Evaluación de victoria (El objetivo final)
        if celda_destino == 'meta':
            return 1000  # Recompensa máxima, gana el juego
        
        # 4. Penalización por ineficiencia (Evitar dar vueltas en círculos)
        # Calculamos matemáticamente cuál sería la coordenada si tomamos esta acción
        desplazamiento_fila, desplazamiento_col = self.DELTAS[accion]
        pos_futura = (pos_actual[0] + desplazamiento_fila, pos_actual[1] + desplazamiento_col)
        
        # Obtenemos cuántas veces hemos pisado esa celda futura (0 si es nueva)
        veces_visitada = self.conteo_visitas.get(pos_futura, 0)
        
        # Multiplicamos el castigo. 1 vez = -100, 2 veces = -200, etc.
        utilidad -= (100 * veces_visitada)

        return utilidad

    def decidir(self, percepcion):
        
        """
        Decide la siguiente acción del agente.
        
        Parámetros:
            percepcion – diccionario con lo que el agente puede ver

        Retorna:
            'arriba', 'abajo', 'izquierda' o 'derecha'
        """
        # ╔══════════════════════════════════════╗
        # ║   ESCRIBE TU LÓGICA AQUÍ             ║
        # ╚══════════════════════════════════════╝

        # Ejemplo básico (bórralo y escribe tu propia lógica):
        #
        # vert, horiz = percepcion['direccion_meta']
        #
        # if percepcion[vert] == 'libre' or percepcion[vert] == 'meta':
        #     return vert
        # if percepcion[horiz] == 'libre' or percepcion[horiz] == 'meta':
        #     return horiz
        #
        # return 'abajo'
        print('Hola decidir')
        for direccion in self.ACCIONES:
            celda = percepcion[direccion]
            if celda == 'meta':
                return direccion
            if celda == 'libre':
                return direccion

        return 'abajo'  # ← Reemplazar con tu lógica