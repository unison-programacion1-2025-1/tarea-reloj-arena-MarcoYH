def reloj_arena(m, s):
    # Dibujar la parte superior del reloj (triángulo decreciente)
    for i in range(m):
        # Calcular espacios y caracteres para cada línea
        espacios = i
        caracteres = 2 * (m - i) - 1
        
        # Imprimir línea: espacios + caracteres
        print(" " * espacios + s * caracteres)
    
    # Dibujar la parte inferior del reloj (triángulo creciente)
    for i in range(1, m):  # Comenzamos desde 1 hasta m-1
        # Calcular espacios y caracteres para cada línea
        espacios = m - i - 1
        caracteres = 2 * (i + 1) - 1
        
        # Imprimir línea: espacios + caracteres
        print(" " * espacios + s * caracteres)
