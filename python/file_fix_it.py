
def get_suffixes(directory):
    suffixes = ["/".join(directory.split('/')[:x + 2]) for x in range(directory.count('/'))]
    return suffixes

def missing_paths(existing, needed):
    to_create = set()
    for directory in needed:
        suffixes = get_suffixes(directory)
        to_create.update(suffixes)
    existing_suffixes = set()
    for directory in existing:
        suffixes = get_suffixes(directory)
        existing_suffixes.update(suffixes)
    return len(to_create - existing_suffixes)


print missing_paths([], ['/home/gcj/finals', '/home/gcj/quals'])
print missing_paths(['/chicken', '/chicken/egg'], ['/chicken'])
print missing_paths(['/a'], ['/a/b', '/a/c', '/b/b'])

if __name__ == '__main__':
    lines = []
    with open('python/codejam/round1b2010/A-large-practice.in') as f:
        for line in f:
            lines.append(line.strip())
    with open('python/codejam/round1b2010/A-large-practice.out', 'w+') as f:
        total_lines = int(lines[0].strip())
        i = 1
        for x in xrange(total_lines):
            N = int(lines[i].split()[0])
            M = int(lines[i].split()[1])
            existing = []
            needed = []
            i += 1
            for n in range(N):
                existing.append(lines[i])
                i += 1
            for m in range(M):
                needed.append(lines[i])
                i += 1

            result = 'Case #%s: %s\n' % (x + 1, missing_paths(existing, needed))
            f.write(result)
