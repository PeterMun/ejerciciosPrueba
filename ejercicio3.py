class BicycleLock:
    def makeDistinct(self, dials):
        acciones = []
        vista = set()

        for i, dial in enumerate(dials):
            if dial in vista:
                ajustes = 1
                while (dial + ajustes) % 10 in vista or (dial - ajustes) % 10 in vista:
                    ajustes += 1
                if (dial + ajustes) % 10 not in vista:
                    acciones.extend(['>'] * i + ['+'] * ajustes)
                    dials[i] = (dial + ajustes) % 10
                else:
                    acciones.extend(['>'] * i + ['-'] * ajustes)
                    dials[i] = (dial - ajustes) % 10
                
                acciones.extend(['<'] * i)
            
            vista.add(dials[i])

        return acciones
bicycleLock = BicycleLock()
dials = list(map(int, input("Ingrese los dígitos de los diales separados por espacio: ").split()))
acciones = bicycleLock.makeDistinct(dials)
print("Acciones:", ' '.join(acciones))
