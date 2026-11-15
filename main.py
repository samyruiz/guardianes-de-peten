"""
Programa Principal: main.py
Sistema de Monitoreo de Fauna - Guardianes del Petén
Entrega 5 — Recursividad: Zonas dentro de zonas (Árbol territorial)

Orden estricto de pruebas solicitado en la Entrega 5:
1. Armar un mapa de al menos 3 niveles debajo de la reserva (zona -> sector -> aguada)
   y al menos 6 zonas en total (validando la guarda R5 para tipos de subzona).
2. Ubicar al menos 5 animales en niveles distintos, con al menos uno en el nivel más profundo.
3. Imprimir el mapa completo con mostrar().
4. Imprimir cuántos animales hay en toda la reserva y en una zona que tenga sectores.
5. Buscar 3 sectores con buscar_sector(): uno del nivel más profundo, uno de primer nivel
   y uno que no existe, e imprimir lo que devolvió cada búsqueda.
6. Comprobar que todo lo de las Entregas 1 a 4 sigue funcionando correctamente.
"""

from animal import Animal
from jaguar import Jaguar
from tapir import Tapir
from guacamaya_roja import GuacamayaRoja
from cocodrilo_de_pantano import CocodriloDePantano
from mono_arana import MonoArana

from sistema_monitoreo import SistemaMonitoreo
from zona import Zona
from guardarrecursos import Guardarrecursos
from collar import Collar
from alerta import Alerta

def separador(titulo: str):
    print("\n" + "=" * 82)
    print(f" {titulo.upper()}")
    print("=" * 82)

def main():
    print("=" * 82)
    print("   UNIVERSIDAD DA VINCI DE GUATEMALA · FACULTAD DE INGENIERÍA")
    print("   FUNDAMENTOS DE PROGRAMACIÓN 2 | ENTREGA 5: RECURSIVIDAD (ZONAS EN ZONAS)")
    print("   SISTEMA DE MONITOREO DE FAUNA: GUARDIANES DEL PETÉN")
    print("=" * 82)

    sistema = SistemaMonitoreo()

    # =========================================================================
    # PASO 1: ARMAR EL MAPA JERÁRQUICO DE LA RESERVA (3 NIVELES, 8 ZONAS EN TOTAL)
    # Nivel 0 (Zona de primer nivel) -> Nivel 1 (Sector) -> Nivel 2 (Aguada / Subsector)
    # =========================================================================
    separador("1. Construcción del Mapa Jerárquico (3 Niveles: Zona -> Sector -> Aguada)")

    # Zonas de Primer Nivel (Nivel 0)
    z_laguna_tigre = Zona("Laguna del Tigre", "núcleo")
    z_mirador = Zona("Mirador-Río Azul", "núcleo")
    z_uaxactun = Zona("Uaxactún", "uso múltiple")

    # Sectores de Segundo Nivel (Nivel 1)
    s_paso_caballos = Zona("Sector Paso Caballos", "amortiguamiento")
    s_el_peru = Zona("Sector El Perú-Waka'", "núcleo")
    s_dos_lagunas = Zona("Sector Dos Lagunas", "núcleo")

    # Aguadas de Tercer Nivel - Nivel más profundo (Nivel 2)
    a_sibal = Zona("Aguada El Sibal", "núcleo")
    a_escondida = Zona("Aguada La Escondida", "núcleo")

    # Armado del árbol con agregar_subzona()
    # Laguna del Tigre -> Sector Paso Caballos y Sector El Perú-Waka' -> Aguada El Sibal y Aguada La Escondida
    s_el_peru.agregar_subzona(a_sibal)
    s_el_peru.agregar_subzona(a_escondida)
    z_laguna_tigre.agregar_subzona(s_paso_caballos)
    z_laguna_tigre.agregar_subzona(s_el_peru)

    # Mirador-Río Azul -> Sector Dos Lagunas
    z_mirador.agregar_subzona(s_dos_lagunas)

    # Registro de las zonas de primer nivel en el sistema central
    sistema.agregar_zona_raiz(z_laguna_tigre)
    sistema.agregar_zona_raiz(z_mirador)
    sistema.agregar_zona_raiz(z_uaxactun)

    print("   [+] Mapa jerárquico estructurado exitosamente con 8 zonas en 3 niveles.")
    print("   -> Verificación de Guarda R5 al intentar agregar una subzona con tipo inválido:")
    subzona_invalida = Zona("Sector Comercial Ilegal", "urbana")
    z_uaxactun.agregar_subzona(subzona_invalida)

    # =========================================================================
    # PASO 2: CREAR Y UBICAR AL MENOS 5 ANIMALES EN NIVELES DISTINTOS
    # (Con al menos uno en el nivel más profundo: Aguada El Sibal / Aguada La Escondida)
    # =========================================================================
    separador("2. Registro y Ubicación de 6 Animales en Distintos Niveles del Árbol")

    balam = Jaguar("JAG-001", "Balam", "rosetas cerradas dobles", 54.5)
    tziquin = Tapir("TAP-001", "Tziquin", 18.5, 215.0)
    kinich = GuacamayaRoja("GUA-001", "K'inich", 98.5, "Cantemó (Metopium brownei)")
    sobek = CocodriloDePantano("COC-001", "Sobek", 2.85, "Laguna del Tigre")
    kaax = MonoArana("MON-001", "Ka'ax", 82.0, 14)
    ixchel = Jaguar("JAG-002", "Ixchel", "rosetas abiertas finas", 46.0)

    for a in [balam, tziquin, kinich, sobek, kaax, ixchel]:
        sistema.registrar_animal(a)

    # Ubicación en niveles distintos del árbol:
    # Nivel 0 (Primer nivel):
    z_laguna_tigre.ubicar(sobek)    # Cocodrilo Sobek en Laguna del Tigre (Nivel 0)
    z_uaxactun.ubicar(kaax)         # Mono araña Ka'ax en Uaxactún (Nivel 0)

    # Nivel 1 (Segundo nivel - Sectores):
    s_paso_caballos.ubicar(kinich)  # Guacamaya K'inich en Sector Paso Caballos (Nivel 1)
    s_dos_lagunas.ubicar(ixchel)    # Jaguar Ixchel en Sector Dos Lagunas (Nivel 1)

    # Nivel 2 (Tercer nivel - Nivel más profundo: Aguadas):
    a_sibal.ubicar(balam)           # Jaguar Balam en Aguada El Sibal (Nivel 2)
    a_escondida.ubicar(tziquin)     # Tapir Tziquin en Aguada La Escondida (Nivel 2)

    print("\n   [+] 6 animales ubicados en los Niveles 0 (Zona), 1 (Sector) y 2 (Aguada).")

    # =========================================================================
    # PASO 3: IMPRIMIR EL MAPA COMPLETO CON mostrar() (RECURSIVO)
    # =========================================================================
    separador("3. Impresión Recursiva del Mapa Completo con mostrar(nivel=0)")
    sistema.mostrar_mapa()

    # =========================================================================
    # PASO 4: CONTAR ANIMALES DE FORMA RECURSIVA CON contar_animales()
    # =========================================================================
    separador("4. Conteo Recursivo de Animales con contar_animales()")

    total_reserva = sistema.contar_animales()
    total_laguna_tigre = z_laguna_tigre.contar_animales()
    total_sector_peru = s_el_peru.contar_animales()
    total_mirador = z_mirador.contar_animales()

    print(f"   • Total de animales en TODA la Reserva de la Biosfera Maya : {total_reserva} animales")
    print(f"   • Total en zona con sectores '{z_laguna_tigre.nombre}' (incluye subzonas): {total_laguna_tigre} animales")
    print(f"     -> Desglose: 1 directo en '{z_laguna_tigre.nombre}' + 1 en '{s_paso_caballos.nombre}' + {total_sector_peru} en '{s_el_peru.nombre}' (sus 2 aguadas)")
    print(f"   • Total en zona con sectores '{z_mirador.nombre}' (incluye subzonas)  : {total_mirador} animal(es)")

    # =========================================================================
    # PASO 5: BUSCAR TRES SECTORES DE FORMA RECURSIVA CON buscar_sector(nombre)
    # 1. Uno del nivel más profundo ("Aguada El Sibal")
    # 2. Uno de primer nivel ("Laguna del Tigre")
    # 3. Uno que no existe ("Sector Fantasma")
    # =========================================================================
    separador("5. Búsqueda Recursiva de Sectores con buscar_sector(nombre)")

    print("[Búsqueda 1] Sector del NIVEL MÁS PROFUNDO ('Aguada El Sibal'):")
    res_profundo = sistema.buscar_sector("Aguada El Sibal")
    print(f"   Resultado devuelto: {res_profundo}")
    if res_profundo:
        print(f"   Animales ubicados ahí: {[f'{a.nombre} ({a.codigo})' for a in res_profundo.animales]}")

    print("\n[Búsqueda 2] Zona de PRIMER NIVEL ('Laguna del Tigre'):")
    res_primer_nivel = sistema.buscar_sector("Laguna del Tigre")
    print(f"   Resultado devuelto: {res_primer_nivel}")
    if res_primer_nivel:
        print(f"   Total recursivo de animales en esta rama: {res_primer_nivel.contar_animales()}")

    print("\n[Búsqueda 3] Sector que NO EXISTE ('Aguada Perdida del Sur'):")
    res_inexistente = sistema.buscar_sector("Aguada Perdida del Sur")
    print(f"   Resultado devuelto: {res_inexistente}")

    # =========================================================================
    # PASO 6: COMPROBACIÓN DE CONTINUIDAD (ENTREGAS 1, 2, 3 Y 4)
    # =========================================================================
    separador("6. Continuidad Operativa de las Entregas 1, 2, 3 y 4")

    # Entrega 4: Ordenamiento por Selección de Alertas y Búsqueda Binaria
    print("--- 6.1 Entrega 4: Ordenamiento de Alertas (Selection Sort) y Búsqueda Binaria ---")
    sistema.alertas = [
        Alerta(1, "batería baja", "media", "Collar COL-02 con 7%", hora="15:20"),
        Alerta(2, "acercamiento a comunidad", "alta", "Jaguar Balam en Uaxactún", hora="18:45"),
        Alerta(3, "acercamiento a comunidad", "alta", "Mono araña Ka'ax en caserío", hora="07:10")
    ]
    sistema.ordenar_alertas()
    for al in sistema.alertas:
        print(f"   {al}")

    busqueda_bin = sistema.buscar_animal("JAG-001")
    print(f"   [Búsqueda Binaria 'JAG-001']: Encontrado -> {busqueda_bin.nombre} ({busqueda_bin.__class__.__name__})")

    # Entrega 3: Ciclo Polimórfico y Clase Abstracta Animal
    print("\n--- 6.2 Entrega 3: Ciclo Polimórfico (describir()) y Clase Abstracta ---")
    for an in [balam, tziquin]:
        print(an.describir())
    try:
        Animal("ANI-000", "Genérico", "desconocido", False)
    except TypeError as e:
        print(f"   [TypeError Clase Abstracta Validado]: {e}")

    # Entregas 1 y 2: Telemetría, Collares, Guardas y Sectores profundos
    print("\n--- 6.3 Entregas 1 y 2: Telemetría GPS sobre el Árbol de Zonas y Guardas ---")
    gr = Guardarrecursos("GR-07", "Don Mateo Chayax")
    sistema.guardarrecursos.append(gr)
    sistema.guardarrecursos_turno = gr

    col1 = Collar("COL-01", bateria=90)
    sistema.collares.append(col1)
    sistema.asignar_collar("COL-01", "JAG-001")

    # Reporte de posición directamente en la aguada del tercer nivel ("Aguada El Sibal")
    sistema.reportar_posicion("COL-01", "Aguada El Sibal", "16:30")
    # Reporte en zona de uso múltiple ("Uaxactún") dispara alerta alta y SMS
    sistema.reportar_posicion("COL-01", "Uaxactún", "19:00")

    print("\n" + "=" * 82)
    print("   EJECUCIÓN DE LA ENTREGA 5 FINALIZADA CON ÉXITO TOTAL")
    print("=" * 82)

if __name__ == "__main__":
    main()
