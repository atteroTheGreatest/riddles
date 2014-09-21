
def make_it_smooth(pixels, delete, insert, max_difference):
    cache = {}

    def solve(pixels, final_value):
        if not pixels:
            return 0

        N = len(pixels)
        best = solve(pixels[:N - 1], final_value) + delete
        key = (len(pixels), final_value)
        if key in cache:
            return cache[key]

        for x in range(256):
            result = solve(pixels[:N - 1], x)
            move_cost = abs(x - pixels[N-1])
            insert_number = abs(final_value - x - 1) / max_difference
            best = min(result + move_cost + insert_number * insert, best)

        cache[key] = best
        return best

    return solve(pixels[:len(pixels) - 1], pixels[-1])

print make_it_smooth([1, 50, 7], 100, 1, 5)
print make_it_smooth([1, 7, 5], 6, 6, 2)
