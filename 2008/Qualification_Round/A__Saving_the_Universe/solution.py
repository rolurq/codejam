def solve(engines: set, queries: list):
    switches = 0

    while queries:
        engine_index = {}
        max_index = -1
        for i, query in enumerate(queries):
            if query in engine_index:
                continue
            
            if query in engines:
                engine_index[query] = i
                max_index = max(max_index, i)

        valid = engines.difference(engine_index.keys())
        if valid:
            return switches

        queries = queries[max_index:]
        switches += 1

    return switches

def main():
    N = int(input())

    for i in range(N):
        S = int(input())
        engines = {input() for _ in range(S)}
        Q = int(input())
        queries = [input() for _ in range(Q)]

        result = solve(engines, queries)
        print("Case #%d: %d" % (i + 1, result))

if __name__ == '__main__':
    import sys
    from os import path
    
    file_input_name = sys.argv[1] if len(sys.argv) > 1 else 'small.in'
    
    if not path.isabs(file_input_name):
        cur_dir = path.dirname(__file__)
        file_input_name = path.join(cur_dir, file_input_name)
    
    file_input = open(file_input_name)
    file_output = open(path.join(cur_dir, "out"), 'w+')
    sys.stdin = file_input
    sys.stdout = file_output
    
    main()