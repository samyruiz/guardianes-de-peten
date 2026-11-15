"""
Módulo que define la clase Zona (Entrega 5: Recursividad — Zonas dentro de zonas).
Representa una delimitación territorial dentro de la Reserva de la Biosfera Maya
que puede contener subzonas (sectores, aguadas, etc.) y animales ubicados en ella.
Tipos válidos según Art. 5 (Guarda R5): 'núcleo', 'amortiguamiento', 'uso múltiple'.
"""

class Zona:
    TIPOS_VALIDOS = ("núcleo", "amortiguamiento", "uso múltiple")

    def __init__(self, nombre: str, tipo_zona: str):
        self.nombre = nombre
        self.tipo_zona = tipo_zona.strip().lower()
        self.subzonas = []   # Lista de objetos Zona que están dentro de esta zona
        self.animales = []   # Lista de objetos Animal que están ubicados en esta zona

    @staticmethod
    def validar_tipo_zona(tipo_zona: str) -> bool:
        """Guarda R5 (Art. 5): Verifica que el tipo de zona sea núcleo, amortiguamiento o uso múltiple."""
        return tipo_zona.strip().lower() in Zona.TIPOS_VALIDOS

    def agregar_subzona(self, zona) -> bool:
        """
        Agrega una subzona a la lista de subzonas de esta zona.
        El tipo de cada subzona pasa por la guarda R5 (Art. 5).
        """
        if not isinstance(zona, Zona) or not self.validar_tipo_zona(zona.tipo_zona):
            tipo_invalido = getattr(zona, 'tipo_zona', str(zona))
            print(f"Rechazado: Tipo de subzona '{tipo_invalido}' inválido para '{ getattr(zona, 'nombre', '') }'. "
                  f"Solo se permiten: núcleo, amortiguamiento o uso múltiple. [Guarda R5 / Art. 5]")
            return False
        self.subzonas.append(zona)
        return True

    def ubicar(self, animal) -> bool:
        """Ubica un animal directamente en la lista de animales de esta zona."""
        self.animales.append(animal)
        return True

    def mostrar(self, nivel: int = 0):
        """
        Muestra el mapa jerárquico de forma recursiva.
        Imprime la zona con una sangría de dos espacios por cada nivel
        y después se llama a sí mismo con cada subzona usando nivel + 1.
        """
        sangria = "  " * nivel
        nombres_animales = ", ".join([f"{a.nombre} ({a.codigo})" for a in self.animales])
        info_animales = f" -> Animales aquí [{len(self.animales)}]: {nombres_animales}" if self.animales else " -> [Sin animales en este nivel]"
        print(f"{sangria}- {self.nombre} (Tipo: {self.tipo_zona}){info_animales}")

        for subzona in self.subzonas:
            subzona.mostrar(nivel + 1)

    def contar_animales(self) -> int:
        """
        Cuenta recursivamente los animales de esta zona más los de todas sus subzonas,
        llamándose a sí mismo con cada subzona.
        """
        total = len(self.animales)
        for subzona in self.subzonas:
            total += subzona.contar_animales()
        return total

    def buscar_sector(self, nombre: str):
        """
        Busca recursivamente una zona o sector por su nombre en el árbol.
        Caso base: Si esta zona se llama así, se devuelve ella misma (self).
        Paso recursivo: Le pregunta a cada subzona y devuelve la primera respuesta que no sea None.
        Si no lo encuentra en ningún lado, devuelve None.
        """
        if self.nombre.lower() == nombre.strip().lower():
            return self

        for subzona in self.subzonas:
            encontrado = subzona.buscar_sector(nombre)
            if encontrado is not None:
                return encontrado

        return None

    def __str__(self):
        return f"Zona: {self.nombre} (Tipo: {self.tipo_zona} | Subzonas directas: {len(self.subzonas)} | Animales directos: {len(self.animales)})"
