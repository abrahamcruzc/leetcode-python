class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        if len(needle) > len(haystack):
            return -1

        base = 256 # Número de caracteres en ASCCI
        prime = 101 # Número primo para reducir colisiones
        n, m = len(haystack), len(needle)
        hash_haystack = hash_needle = 0
        h = 1 # Factor de mayor peso  en el hash rodante

        # Precomputar el factor de mayor peso
        for _ in range(m - 1):
            h = (h * base) % prime

        # Calcular los hashes iniciales
        for i in range(m):
            hash_needle = (base * hash_needle + ord(needle[i])) % prime
            hash_haystack = (base * hash_haystack + ord(haystack[i])) % prime

        # Delizar la ventana
        for i in range(n -m + 1):
            if hash_haystack == hash_needle: # Posible coincidencia
                if haystack[i:i + m] == needle:
                    return i

            if i < n - m:
                # Actualizar el hash usando hash rodante
                hash_haystack = (base * (hash_haystack - ord(haystack[i]) * h) + ord(haystack[i + m])) % prime
                if hash_haystack < 0:
                    hash_haystack += prime # Asegurar que el hash sea positivo


        return -1

haystack: str = "aldkajflsjfkasadajagh"
needle: str = "sad"

sol: Solution = Solution()
result: int = sol.strStr(haystack, needle)
print(result)
